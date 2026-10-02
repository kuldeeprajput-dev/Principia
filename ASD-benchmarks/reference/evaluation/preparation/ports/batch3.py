"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io
from .mat_native import load
SEED = 'principia-ASD-batch3-20260930-before-fit-v1'

def key(s):
    return hashlib.sha256((SEED + '|' + s).encode()).hexdigest()

def rheo():
    z = zipfile.ZipFile(next(DATA.glob('57_*/raw/*.zip')))
    names = sorted((n for n in z.namelist() if n.endswith('.csv')))
    meta = {}
    groups = {}
    allrows = []
    status = {}
    ranges = []
    for n in names:
        s = z.read(n).decode('utf-16')
        uid = re.search('^Test ID:\\t([^\\t]+)', s, re.M).group(1)
        form = 'neat' if 'Neat' in n or 'neat' in n else re.search('(0_\\d+gcc_\\d+%)', n).group(1)
        groups.setdefault(form, []).append(uid)
        meta[uid] = (n, s, form)
    for form, uu in groups.items():
        ordered = sorted(uu, key=key)
        audited = [u for u in uu if meta[u][0] == names[0]]
        pool = [u for u in ordered if u not in audited]
        held = pool[0]
        dev = sorted([u for u in uu if u != held], key=key)
        for u in uu:
            n, s, _ = meta[u]
            part = 'confirmation' if u == held else 'development'
            fold = -1 if u == held else dev.index(u)
            block = 0
            expected = False
            for li, l in enumerate(s.splitlines(), 1):
                if l.startswith('Result:\t'):
                    block += 1
                if l.startswith('\tPoint No.') or l.startswith('\tPoint No\t'):
                    expected = True
                cs = l.split('\t')
                if len(cs) == 7 and cs[0] == '' and cs[1].isdigit():
                    try:
                        T, eta, gamma = (float(cs[2]), float(cs[3]), float(cs[5]))
                    except ValueError:
                        continue
                    assert gamma > 0 and -100 < T < 300
                    status[cs[4]] = status.get(cs[4], 0) + 1
                    allrows.append(dict(sample_id=f'{u}:{li}', group=u, partition=part, fold=fold, formulation=form, T_C=T, shear_s=gamma, target=eta, source_member=n, source_line=li, source_block=block, status=cs[4]))
    audit = dict(source='Zenodo 19699588, NYU Anton Paar RheoCompass exports', measurement_dates='Native metadata 2024–2025; release 2026-04-22', native_format='UTF-16 tab-separated exports with .csv suffix; 50 independent Test IDs, 10 formulations, five tests per formulation', units={'viscosity': 'cP', 'temperature': 'degC', 'shear_rate': 's^-1'}, processing='Parse native numeric rows only; no smoothing, imputation or log-based target exclusion. All temperatures/rates in each Test ID stay together.', flags=status, limitations=['Nominal loading percent basis is unspecified; use formulation labels rather than a mass/volume constitutive inference.', 'Heating order, aging and temperature are confounded.', 'Native result-count metadata may say14 while table contains10 blocks.', 'Tests are repeated within formulations, not demonstrated independent synthesis lots.'], audit_exposure='One inspected file with first low-temperature responses was excluded from the reserved pool. Target-independent metadata hash chooses one complete test per formulation; no confirmation score was opened.')
    save(57, allrows, audit, ['formulation', 'T_C', 'shear_s'], dict(formulation='source label; calibrated category', T_C='degC', shear_s='s^-1', target='cP'), 'Native dynamic viscosity')

def acoustic():
    ps = sorted(next(DATA.glob('60_*')).glob('raw/*.mat'))
    widths = sorted({int(re.search('_w(\\d+)', p.name).group(1)) for p in ps})
    held = sorted(widths, key=lambda w: key('60width' + str(w)))[0]
    dev = [w for w in widths if w != held]
    rows = []
    anomalies = []
    dates = []
    for p in ps:
        d = load(p)['dataset']
        a = d['tst']['s07']
        w = int(re.search('_w(\\d+)', p.name).group(1))
        dist = int(re.search('_d(\\d+)', p.name).group(1))
        freq = int(re.search('_f(\\d+)', p.name).group(1))
        t = a['d12']['v'].reshape(-1)
        v = a['d13']['v']
        assert v.shape[0] == len(t) and np.all(np.diff(t) > 0)
        nominal = float(a['d06']['v'].item())
        assert np.isclose(nominal, w * 1e-07)
        assert str(a['d13']['u']).strip() == 'V'
        if int(a['d10']['v'].item()) != v.shape[1]:
            anomalies.append({'file': p.name, 'declared_signals': int(a['d10']['v'].item()), 'actual_columns': v.shape[1]})
        for col in range(v.shape[1]):
            baseline = float(v[t < 0, col].mean())
            peak = float(np.max(abs(v[t >= 0, col] - baseline)))
            rows.append(dict(sample_id=f'{p.name}:s07:{col + 1}', group=p.name, partition='confirmation' if w == held else 'development', fold=-1 if w == held else dev.index(w), condition=f'd{dist}_f{freq}', distance_mm=dist, resonance_kHz=freq, width_us=nominal * 1000000.0, target=peak, source_file=p.name, source_channel='s07', source_column=col + 1, pretrigger_mean_V=baseline))
    audit = dict(source='Zenodo 17266427; TU Graz Jakob Harden, converted MATLABv6 exports', measurement_dates='Native embedded measurement timestamps in 2020; technical description 2023, MAT export 2025. Export date is not acquisition date.', native_format='36 MATLAB5/6 datasets; constrained byte-level MAT parser handles Octave UTF-8 metadata incompatibility with SciPy', processing='Target is maximum absolute receiver voltage across all t>=0 samples, subtracting each trace mean over t<0. No response-selected time window or denoising. Ten actual waveform columns kept per file.', unit='V', inconsistencies=anomalies, limitations=['Native pulse width in SI seconds overrides inconsistent PDF typography; w125 means12.5 us.', 's07 is a nominal shear-type receiver measuring in air: no shear-wave propagation through air is asserted.', 'Nominal resonance and sensor identity are confounded.', 'Zero-distance contact is a different coupling regime.', 'Repeated pulses within one source run are not independent devices.'], audit_exposure='Only numerical schema/sample metadata were inspected before fitting. The reserved pulse width is allocated by metadata hash. No final performance inspected.')
    save(60, rows, audit, ['condition', 'distance_mm', 'resonance_kHz', 'width_us'], dict(condition='calibrated distance/sensor label', distance_mm='mm', resonance_kHz='kHz; confounded with sensor type', width_us='us', target='V'), 'Post-trigger peak absolute receiver voltage')

def yeast():
    p = next(DATA.glob('72_*/raw/*.xlsx'))
    w = openpyxl.load_workbook(p, read_only=True, data_only=True)
    wf = openpyxl.load_workbook(p, read_only=True, data_only=False)
    strains = [s.title for s in list(w)[2:]]
    held = sorted(strains, key=lambda s: key('72strain' + s))[:2]
    dev = [s for s in strains if s not in held]
    rows = []
    omitted = []
    ambiguities = []
    for s in list(w)[2:]:
        rr = list(s.values)
        ff = list(wf[s.title].values)
        ix = 4 if s.title == 'GRE' else 3
        pc = 14 if s.title == 'GRE' else 12 if s.title == 'Clos' else 13
        samples = {}
        chart = None
        for li, row in enumerate(rr, 1):
            m = re.fullmatch('R([123])(\\d+)', str(row[ix]))
            if not m:
                continue
            rep, t = (int(m[1]), int(m[2]))
            formula = ff[li - 1][pc]
            assert isinstance(formula, str) and '*100' in formula, (s.title, li, pc, formula)
            if row[1] is not None:
                chart = float(re.search('\\d+', str(row[1])).group())
            if chart != t:
                ambiguities.append(dict(strain=s.title, row=li, sample_time=t, chart_time=chart))
                continue
            samples[rep, t] = (float(row[pc]), li)
        for rep in [1, 2, 3]:
            if (rep, 22) not in samples or (rep, 72) not in samples:
                omitted.append(dict(strain=s.title, replicate=rep, reason='missing22 or72 hour prefix'))
                continue
            p22 = samples[rep, 22][0]
            p72 = samples[rep, 72][0]
            for (r, t), (y, li) in samples.items():
                if r != rep or t < 96:
                    continue
                rows.append(dict(sample_id=f'{s.title}:row{li}', group=s.title, partition='confirmation' if s.title in held else 'development', fold=-1 if s.title in held else dev.index(s.title), p22_pct=p22, p72_pct=p72, time_h=t, target=y, replicate=rep, source_file=p.name, source_sheet=s.title, source_row=li, source_column=openpyxl.utils.get_column_letter(pc + 1)))
    audit = dict(source='Zenodo 18757697, IATA-CSIC competition with S.kudriavzevii CR85; linked study doi10.1016/j.fm.2023.104276', measurement_dates='Native qPCR exports 2020; workbook analytical sections 2021/2022; public deposit2026', processing='Author cached spreadsheet percentage from same-row qPCR ratio is the target. No same-time Cp/ratio is a predictor. Use only own replicate22/72-hour percentages to forecast96h and later. Biological replicate pairing from Sample Name.', missing_prefix=omitted, excluded_ambiguous_time=ambiguities, limitations=['qPCR percentage is author-derived abundance, not independently measured fitness or viable count.', 'Nitrogen description300 g/L is unresolved; unused.', 'Source previous published competition analyses disclosed.', 'Only two reserved strain groups, small within-campaign scope.'], audit_exposure='Schema audit printed first13 spreadsheet rows before model construction, including several later percentages across all strains. Allocation is still metadata-only and no fit/selection uses reserved targets, but confirmation is audit-exposed retrospective evidence, not a fully blind independent confirmation.')
    save(72, rows, audit, ['p22_pct', 'p72_pct', 'time_h'], dict(p22_pct='percentage points; own replicate at22h', p72_pct='percentage points; own replicate at72h', time_h='h since inoculation', target='percentage points'), 'Later author qPCR S.kudriavzevii percentage')

def hive():
    rows = []
    omitted = {}
    bounds = {}
    for p in sorted(next(DATA.glob('83_*')).glob('raw/*.csv')):
        if 'Pluviom' in p.name:
            continue
        d = pd.read_csv(p)
        d['row'] = np.arange(len(d)) + 2
        d['dt'] = pd.to_datetime(d.time, format='mixed')
        for sid, v in d.groupby('id_sensor'):
            v = v.sort_values('dt').reset_index(drop=True)
            stream = f'{p.stem}:sensor{sid}'
            days = sorted(v.dt.dt.strftime('%Y-%m-%d').unique())
            cut = max(1, int(len(days) * 0.8))
            bound = days[cut]
            bounds[stream] = bound
            devdays = days[:cut]
            origins = v.groupby(v.dt.dt.floor('h'), sort=True).head(1)
            origins = origins[(origins.dt - origins.dt.dt.floor('h')).dt.total_seconds() <= 900]
            times = v.dt.to_numpy(dtype='datetime64[ns]').astype('int64')
            temp = v.temperature.to_numpy(float)
            ext = v.ext_temperature.to_numpy(float)
            rh = v.ext_humidity.to_numpy(float)
            for ri, r in origins.iterrows():
                now = times[ri]
                wanted = now + 3600 * 10 ** 9
                k = np.searchsorted(times, wanted)
                pool = [j for j in [k - 1, k] if 0 <= j < len(v)]
                j = min(pool, key=lambda j: abs(times[j] - wanted))
                lag = np.searchsorted(times, now - 3600 * 10 ** 9, side='right') - 1
                day = r['dt'].strftime('%Y-%m-%d')
                reason = None
                if abs(times[j] - wanted) > 300 * 10 ** 9:
                    reason = 'no target within5min'
                elif v.dt.iloc[j].strftime('%Y-%m-%d') != day:
                    reason = 'cross-day target'
                elif lag < 0 or now - 3600 * 10 ** 9 - times[lag] > 900 * 10 ** 9:
                    reason = 'missing causal one-hour lag'
                elif not np.isfinite([temp[ri], temp[lag], ext[ri], rh[ri]]).all():
                    reason = 'missing input'
                elif not (0 <= temp[ri] <= 60 and 0 <= temp[lag] <= 60 and (-10 <= ext[ri] <= 60) and (0 <= rh[ri] <= 100)):
                    reason = 'fixed input domain bounds'
                if reason:
                    omitted[reason] = omitted.get(reason, 0) + 1
                    continue
                part = 'confirmation' if day >= bound else 'development'
                di = days.index(day)
                fold = -1 if part == 'confirmation' else min(3, di * 4 // cut)
                hour = r['dt'].hour + r['dt'].minute / 60
                rows.append(dict(sample_id=f'{stream}:row{int(r.row)}->row{int(v.row.iloc[j])}', group=f'{stream}:{('future' if part == 'confirmation' else 'block' + str(fold))}', partition=part, fold=fold, stream=stream, T_now=temp[ri], T_lag=temp[lag], T_external=ext[ri], RH_external=rh[ri], hour_sin=np.sin(2 * np.pi * hour / 24), hour_cos=np.cos(2 * np.pi * hour / 24), target=temp[j], source_file=p.name, source_origin_row=int(r.row), source_target_row=int(v.row.iloc[j]), origin_time=str(r['dt']), target_time=str(v.dt.iloc[j]), lag_time=str(v.dt.iloc[lag]), native_day=day, target_offset_min=(times[j] - now) / 60000000000.0))
    audit = dict(source='Zenodo20399470, Federal University of Ceará apiary', measurement_dates='ApisDec2024–Mar2025; MeliponiniSep2025–Mar2026; releaseMay2026', processing='One hourly origin: first native observation within first15min. Forecast nominal1hour, score nearest native target within5min, same calendar day, no interpolation. Causal lag<=origin−1hour within15min. Latest20percent native dates per stream reserved. Native response outliers retained.', exclusions=omitted, chronological_boundaries=bounds, limitations=['Five sensor streams; independence of Meliponini colonies not proven.', 'Species, period, sensor placement and hive confounded.', 'Naive source clock has no declared timezone.', 'Thermal terms do not identify brood temperature, metabolic heat or ventilation.', 'Daily rainfall could be future information and is excluded.'], audit_exposure='Timestamp/input dictionaries examined; no future confirmation targets or score viewed before protocol freezing.')
    save(83, rows, audit, ['stream', 'T_now', 'T_lag', 'T_external', 'RH_external', 'hour_sin', 'hour_cos'], dict(stream='calibrated sensor label', T_now='degC', T_lag='degC,causal lag1h', T_external='degC,current', RH_external='percent,current', hour_sin='dimensionless source-clock phase', hour_cos='dimensionless source-clock phase', target='degC'), 'One-hour future internal sensor temperature', 'rmse')

def mobile():
    z = zipfile.ZipFile(next(DATA.glob('100_*/raw/*.zip')))
    ns = sorted((n for n in z.namelist() if n.endswith('_ping.csv')))
    routes = {}
    rows = []
    excluded = {}
    held = []
    for n in ns:
        routes.setdefault(n.split('/')[0], []).append(n)
    for route, nn in routes.items():
        pool = [n for n in nn if not ('Indoor (Rectangular' in n and '/1000B/' in n)]
        held.append(sorted(pool, key=key)[0])
    dev = [n for n in ns if n not in held]
    for n in ns:
        d = pd.read_csv(z.open(n))
        a = pd.read_csv(z.open(n.replace('_ping.csv', '_rssi_position.csv')))
        d['native_row'] = np.arange(len(d)) + 2
        d = d.sort_values('Timestamp').reset_index(drop=True)
        a = a.sort_values('Timestamp')
        at = a.Timestamp.to_numpy()
        payload = int(re.search('/(\\d+)B/', n).group(1))
        route = n.split('/')[0]
        tt = d['Ping Time (ms)'].to_numpy(float)
        tm = d.Timestamp.to_numpy(float)
        for k in range(5, len(d)):
            cutoff = tm[k - 1]
            j = np.searchsorted(at, cutoff, side='right') - 1
            reason = None
            if j < 0 or cutoff - at[j] > 0.5:
                reason = 'no causal radio sample within0.5s'
            elif not np.isfinite(tt[k - 5:k]).all():
                reason = 'missing five-probe input prefix'
            elif not np.isfinite(a.iloc[j][['RSRP', 'RSRQ']].to_numpy(float)).all():
                reason = 'missing radio input'
            if reason:
                excluded[reason] = excluded.get(reason, 0) + 1
                continue
            target = tt[k] if not bool(d.Lost.iloc[k]) else np.nan
            rows.append(dict(sample_id=f'{Path(n).stem}:row{int(d.native_row.iloc[k])}', group=Path(n).stem, partition='confirmation' if n in held else 'development', fold=-1 if n in held else dev.index(n), route=route, payload_B=payload, last_rtt=tt[k - 1], mean5_rtt=float(tt[k - 5:k].mean()), mean3_rtt=float(tt[k - 3:k].mean()), trend_rtt=tt[k - 1] - tt[k - 2], RSRP=float(a.RSRP.iloc[j]), RSRQ=float(a.RSRQ.iloc[j]), target=target, source_ping_member=n, source_radio_member=n.replace('_ping.csv', '_rssi_position.csv'), source_ping_row=int(d.native_row.iloc[k]), source_radio_timestamp=at[j], prediction_cutoff=cutoff, target_timestamp=tm[k], lost=bool(d.Lost.iloc[k])))
    audit = dict(source='Zenodo14635635, Vigo/Málaga6G-MOBKPI on6G-SANDBOX platform', measurement_dates='Nov20–22,2024; releaseJan2025', processing='Predict next probe RTT using only five previous completed RTTs and radio asof previous completion, <=0.5s old. No current response-completion timestamp, ICMPseq, cumulative average/loss, future gap, throughput or same-probe radio in inputs. Successful response conditional target; missing lost responses retained when inputs eligible.', exclusions=excluded, reserved_source_runs=held, limitations=['Nine PING runs at one installation; three reserved runs, one per route.', 'Past RTTs in a reserved run are declared online calibration available to all models.', 'Transport timestamp semantics do not establish request send times.', 'RSSI often constant; use only RSRP/RSRQ.', 'Latency is not packet-loss reliability, queue occupancy or identified5G scheduler state.'], audit_exposure='First indoor-rectangle1000B file audit responses viewed; this complete file excluded from reserved allocation. Metadata hash chooses one run per route from remaining source-defined runs.')
    save(100, rows, audit, ['route', 'payload_B', 'last_rtt', 'mean5_rtt', 'mean3_rtt', 'trend_rtt', 'RSRP', 'RSRQ'], dict(route='calibrated route label', payload_B='B', last_rtt='ms,previous completion', mean5_rtt='ms,previous5 completions', mean3_rtt='ms,previous3 completions', trend_rtt='ms,previous RTT difference', RSRP='dBm,asof previouscompletion', RSRQ='dB,asof previouscompletion', target='ms'), 'Next successful ICMP probe RTT')
