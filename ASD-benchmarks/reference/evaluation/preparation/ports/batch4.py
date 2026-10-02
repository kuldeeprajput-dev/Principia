"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys,json,hashlib,re,zipfile,datetime,io,math,time,collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io

def hashgroup(s):
    return hashlib.sha256(('P100-ASD-B4-20261001:' + s).encode()).hexdigest()

def src(i):
    return next(DATA.glob(f'{i:02}_*'))

def text(b):
    return b.decode('utf-16') if b.startswith(b'\xff\xfe') else b.decode('utf-8-sig', errors='replace')

def reserve(groups, n):
    return sorted(sorted(set(groups), key=hashgroup)[:n])
source_urls = {23: 'https://zenodo.org/records/15365365', 52: 'https://zenodo.org/records/15356141', 55: 'https://zenodo.org/records/17092152', 58: 'https://zenodo.org/records/17294879', 59: 'https://data.mendeley.com/datasets/dbh93b6vp8/3', 66: 'https://doi.org/10.57745/KR8BIW', 69: 'https://doi.org/10.18419/DARUS-5015', 78: 'https://zenodo.org/records/15124940', 86: 'https://zenodo.org/records/14619074', 96: 'https://zenodo.org/records/18098714'}

def common(target, units, inputs, semantics, group, scope, timing):
    return dict(target=target, units=units, input_units=inputs, features=list(inputs), semantics=semantics, group_unit=group, scope=scope, timing=timing)

def case23():
    p = src(23) / 'raw'
    d = pd.read_csv(p / 'friction data.dat', skiprows=[1, 2])
    h = pd.read_csv(p / 'participant_hydration_size.dat', sep='\t', skiprows=[1, 2]).set_index('participant')
    rows = []
    for j, r in d.iterrows():
        rows.append(dict(group=str(r['participant']), sample=int(r['sample']), H=float(r['HrVeltkamp']), viscosity=float(r['eta(gamma)']), speed=float(r.velocity), load=float(r.Fz), hydration=float(h.loc[r.participant, 'SC hydration']), area=float(h.loc[r.participant, 'finger pad area']), target=float(r.CoF), anchor=f'friction data.dat:row{j + 4}'))
    output(23, rows, common('Author-derived median coefficient of friction', '1', {'H': 'dimensionless; author Hersey calibration', 'viscosity': 'Pa s at 500 s^-1; author rheology fit', 'speed': 'm/s', 'load': 'N', 'hydration': 'corneometer instrument units', 'area': 'cm^2'}, '165 participant–fluid observations (check actual count); primary response is author-derived median CoF, not instantaneous raw telemetry. Source already reports the Stribeck collapse and hydrodynamic exponent. Area/hydration are separate measurements; author-fit Hersey coefficients cannot validate their own physics. Raw force/position files remain untouched.', 'whole participant', 'One substrate, eleven participants; transfer to reserved people under the same fluid panel, not other surfaces or contact systems. Fluids shared across participants.', 'Conditional prediction at supplied trial-average speed/load. These trial summaries are not prospective controller inputs; no temporal forecasting claim.'))

def case52():
    p = src(52) / 'raw'
    rows = []
    for turbine in [1, 2]:
        d = scipy.io.loadmat(p / f'WT{turbine}_ABL_Type_II.mat', simplify_cells=True)[f'WT{turbine}_ABL_TypeII']
        for name, v in d.items():
            if not isinstance(v, dict) or 'uu' not in v:
                continue
            m = re.search('(Greedy|A2_St\\d+)_(\\d+)D$', name)
            control = m[1]
            xd = int(m[2])
            st = 0 if control == 'Greedy' else int(control[-3:]) / 100
            for j, (y, z, u) in enumerate(zip(v['yy'].ravel(), v['zz'].ravel(), v['uu'].ravel())):
                rows.append(dict(group=control, turbine=turbine, x_D=xd, y_D=float(y) / 0.58, z_D=float(z) / 0.58, St=st, target=float(u) if np.isfinite(u) else np.nan, anchor=f'WT{turbine}_ABL_Type_II.mat:{name}.uu[{j // 21},{j % 21}]'))
    output(52, rows, common('Interpolated time-average streamwise wake velocity', 'm/s', {'turbine': '1 or 2 (within installation)', 'x_D': 'downstream distance/0.58 m rotor diameter', 'y_D': 'lateral coordinate/rotor diameter', 'z_D': 'vertical coordinate/rotor diameter', 'St': 'actuation Strouhal number, 0 labels greedy baseline'}, 'Source-native lidar-derived uu grids; grid cells are correlated interpolated products. Raw vlos retained upstream. Rotor-equivalent wind and virtual turbine power are excluded as targets and predictors. No cubic-power identity is counted as a rule. ABL Type II only.', 'whole control setting across turbines and downstream sections', 'Only four controls and one wind-tunnel system; three development controls and one reserved. Spatial errors describe field interpolation/transfer, not independent grid replicates.', 'Geometry and actuation settings only; no reserved velocity or rotor-equivalent speed is a predictor.'), reserve(['Greedy', 'A2_St025', 'A2_St030', 'A2_St040'], 1))

def case55():
    p = src(55) / 'raw'
    w = openpyxl.load_workbook(p / '08.2025_Rheology tests.xlsx', data_only=True, read_only=True)
    s = w['Slow penetration_Normal Force']
    v = list(s.values)
    rows = []
    for c in range(2, 56, 6):
        label = str(v[0][c])
        nums = re.findall('\\d+\\.?\\d*', label)
        ratio = float(nums[0])
        water = float(nums[1])
        water = water / 100 if water > 1 else water
        group = f'{ratio:.1f}_{water:.2f}'
        for age, offset in [(0, 0), (30, 3)]:
            for rep in [0, 1]:
                for j, row in enumerate(v[3:], start=4):
                    t = row[1]
                    f = row[c + offset + rep]
                    if isinstance(t, (int, float)) and isinstance(f, (int, float)):
                        rows.append(dict(group=group, ratio=ratio, water=water, age_min=age, time_s=float(t), replicate=rep + 1, target=float(f), anchor=f'08.2025_Rheology tests.xlsx:Slow penetration_Normal Force:row{j}:col{c + offset + rep + 1}'))
    output(55, rows, common('Individual penetration normal force', 'N', {'ratio': 'mix-design ratio encoded in author mixture label', 'water': 'water ratio encoded in author mixture label', 'age_min': 'min since mixing; 0 or 30', 'time_s': 'native penetration clock index; unit unspecified'}, 'Two independent trace columns per mixture/age are retained; source average columns excluded. Time header supplies time, without an explicit unit in the workbook; the native penetration clock unit is unresolved; no physical time constant is claimed. Dimensionless t/t_ref used in equations. Mix-label ratio meanings require author PDF; do not call these stress or yield-stress measurements.', 'whole mixture across both ages and replicates', 'Nine mix labels, two batches per mixture/age according to the source PDF, one early research campaign. Force–penetration-time relationships cannot identify intrinsic constitutive stress without probe kinematics/geometry.', 'Known mix label, age and elapsed penetration index only; force is never an input.'))

def case58():
    z = zipfile.ZipFile(next((src(58) / 'raw').glob('*.zip')))
    rows = []
    for n in z.namelist():
        if '/DFS_' not in n or '.TAD' in n:
            continue
        T = int(re.search('_T(\\d+)_', n)[1])
        d = pd.read_csv(io.StringIO(text(z.read(n)).replace('\x00', '')), sep='\t', skiprows=[1])
        for j, r in d.iterrows():
            if pd.notna(r["G'"]):
                rows.append(dict(group=f'T{T}', temperature_C=T, omega=float(r['w']), target=float(r["G'"]), loss_modulus=float(r['G"']), anchor=f'PDLLA15k_DSC_GPC_rheo.zip:{n}:row{j + 3}'))
    sp = common('Storage modulus G prime', 'Pa', {'temperature_C': 'degree C', 'omega': 'rad/s'}, 'Native DFS text exports only; paired TAD exports are linked duplicates, not independent samples. Target storage modulus and secondary loss modulus are separate native instrument outputs, though both share systematic calibration. No compliance correction was applied by the authors. A single purchased polymer batch.', 'whole temperature sweep', 'Temperature transfer within one material; no batch-to-batch or general polymer law claim. Positive modulus spans orders of magnitude.', 'Temperature and imposed frequency only. Loss modulus is withheld as an orthogonal mechanistic check; never a primary predictor.')
    sp['primary_metric'] = 'log_mae'
    output(58, rows, sp)

def case59():
    p = src(59) / 'raw'
    meta = pd.read_excel(p / 'PV Plants Metadata.xlsx', header=1)
    z = zipfile.ZipFile(p / 'weather_files.zip')
    rows = []
    for _, r in meta.iterrows():
        pid = str(int(r['PV Serial Number']))
        loc = r.Location
        cap = float(r['Installed Power (kWp)'])
        limit = float(r['Connection Power (kWn)']) / cap
        d = pd.read_excel(p / 'PV Plants Datasets.xlsx', sheet_name=pid)
        b = z.read(loc + '_weather.csv')
        weather = pd.read_csv(io.BytesIO(b))
        weather['date'] = pd.to_datetime(weather.iloc[:, 0], format='%m/%d/%y %I:%M %p')
        assert weather.date.is_unique
        ww = weather.set_index('date')
        for j, r0 in d.iterrows():
            t = pd.Timestamp(r0['Date'])
            v = ww.loc[t] if t in ww.index else None
            if v is None or not np.isfinite(v.iloc[-1]) or v.iloc[-1] <= 20:
                continue
            rows.append(dict(group=loc, plant=pid, irradiance=float(v.iloc[-1]) / 1000, temp_C=float(v.iloc[1]), wind=float(v.iloc[6]) / 3.6, hour=t.hour, doy=t.dayofyear, limit=limit, latitude=float(r.Latitude), target=float(r0['Produced Energy (kWh)']) / cap if pd.notna(r0['Produced Energy (kWh)']) else np.nan, anchor=f'PV Plants Datasets.xlsx:{pid}:row{j + 2}; weather_files.zip:{loc}_weather.csv:{t.isoformat()}'))
    output(59, rows, common('Hourly produced energy divided by installed capacity', 'kWh/kWp', {'irradiance': 'kW/m^2; supplied weather shortwave radiation', 'temp_C': 'degree C; supplied 2 m temperature', 'wind': 'm/s; supplied 10 m wind converted from km/h', 'hour': 'source-clock hour; no timezone assumed', 'doy': 'calendar day of year', 'limit': 'connection kW / installed kWp', 'latitude': 'degree north'}, 'Native measured energy is divided by independently supplied installed power; source specific-energy and avoided-CO2 columns are excluded. Weather provider/provenance and timezone are unresolved, so the case is mixed measured/author-supplied weather. Daylight cohort fixed by input irradiance >20 W/m^2; no target-based filtering. Missing native energy retained as missing targets. All nine plants and all years retained subject to declared daylight availability.', 'whole city/location', 'Six cities, nine plants; plants within a city share weather and are not independent weather sites. Same-hour conditional energy prediction, not weather forecasting or proven thermal causality.', 'Contemporaneous weather and calendar/plant metadata only; no target energy, source specific-energy or emissions as inputs.'))

def case66():
    p = src(66) / 'raw'
    rows = []
    for f in sorted(p.glob('EXCESS H2 * K--*.csv')):
        T = int(re.search('H2 (\\d+) K', f.name)[1])
        m = re.search('(\\d+)%', f.name)
        eg = int(m[1]) if m else 0
        d = pd.read_csv(f, encoding='utf-8-sig')
        for branch, offset in [('adsorption', 0), ('desorption', 2)]:
            for j, r in d.iterrows():
                if pd.notna(r.iloc[offset]):
                    rows.append(dict(group=f'EG{eg}', eg_pct=eg, temperature_K=T, pressure_bar=float(r.iloc[offset]), branch=1 if branch == 'desorption' else 0, target=float(r.iloc[offset + 1]), anchor=f'{f.name}:row{j + 2}:branch{branch}'))
    output(66, rows, common('Excess hydrogen uptake', 'wt.%', {'eg_pct': 'wt.% expanded graphite in material label', 'temperature_K': 'K', 'pressure_bar': 'bar', 'branch': '0 adsorption, 1 desorption'}, 'Excess uptake is the native experimental response. Total uptake, cyclic reuse files and descriptor curves remain upstream; they are not independent excess-uptake confirmation. Excess adsorption can decline with pressure through gas-volume displacement; a monotone absolute-Langmuir law alone is an intentionally falsifiable baseline.', 'whole material composition across temperatures and both branches', 'Four MOF/graphite compositions and one source campaign. A branch contrast has different sampled pressures and cannot by itself establish irreversible hysteresis.', 'Composition, pressure, temperature, branch only; no measured uptake-derived quantity as an input.'))

def case69():
    p = src(69) / 'raw'
    rows = []
    for f in sorted(p.rglob('*.csv')):
        d = pd.read_csv(f)
        ix = np.flatnonzero(np.r_[True, np.diff(np.floor(d.t.to_numpy() / 5)) > 0])
        d = d.iloc[ix].copy()
        name = str(f.relative_to(p))
        t0 = float(d.iloc[0].T_L)
        for j, r in d.iterrows():
            rows.append(dict(group=name, time_s=float(r.t), housing_C=float(r.T_H), environment_C=float(r.T_E), speed=float(r.theta_dot), friction=float(r.tau_f), initial_C=t0, target=float(r.T_L) if float(r.t) > 0 else np.nan, anchor=f'{name}:row{j + 2}'))
    groups = [r['group'] for r in rows]
    reserved = sorted(set((g for g in groups if g.startswith('validation/'))))
    output(69, rows, common('Lubricant temperature', 'degree C', {'time_s': 's', 'housing_C': 'degree C', 'environment_C': 'degree C', 'speed': 'rad/s', 'friction': 'N m; source friction torque', 'initial_C': 'degree C; explicitly permitted initial lubricant measurement'}, 'Original identification and validation folder assignment preserved. First native sample of each 5 s bin used for compact, deterministic low-frequency thermal analysis; no interpolation. Startup TL is permitted calibration. Neither later lubricant temperatures nor their finite differences enter prediction. Source already presents a lubricant-temperature observer.', 'whole thermal experiment/run', 'Five identification runs and eight source validation runs in one gearbox. Initial calibration and measured housing/friction signals are required; no unseen gearbox or sensorless temperature claim.', 'Causal housing/environment/friction history through current sample plus first lubricant temperature. Exclude t=0 from scoring because it is calibration, not a forecast.'), reserved)

def case78():
    z = zipfile.ZipFile(next((src(78) / 'raw').glob('*.zip')))
    rows = []
    alias = {}

    def norm(v):
        return re.sub('\\s+', '', v).upper()
    for n in z.namelist():
        if not n.endswith('.xlsx') or 'overview' in n:
            continue
        w = openpyxl.load_workbook(io.BytesIO(z.read(n)), read_only=True, data_only=True)
        if 'RefToDict' not in w:
            continue
        vv = list(w['RefToDict'].iter_rows(min_row=1, max_row=100, values_only=True))
        headers = list(vv[0])
        col = headers.index('BACTERIAL_STRAIN_NAME_BACTERIAL_STRAIN_SITE_REF')
        for row in vv[1:]:
            v = str(row[col] or '')
            m = re.match('(KLEPN|PSEAE) DSM\\s*(\\d+)(.*)', v)
            if m and m[3] and (m[3] != '0'):
                a = norm(m[3])
                c = m[1] + ' DSM ' + m[2]
                if a in alias and alias[a] != c:
                    raise ValueError('Conflicting source alias ' + a)
                alias[a] = c
    overview_name = next((n for n in z.namelist() if 'overview' in n and n.endswith('.xlsx')))
    ow = openpyxl.load_workbook(io.BytesIO(z.read(overview_name)), read_only=True, data_only=True)
    study_map = {}
    for row in ow['Overview'].iter_rows(min_row=2, max_row=100, values_only=True):
        if not row[0] or not row[4]:
            continue
        prefix = 'KLEPN' if str(row[0]).startswith('K.') else 'PSEAE'
        canonical_id = re.sub('\\s+', ' ', str(row[2])).strip()
        if canonical_id.lower() == 'na':
            continue
        study_map.setdefault((str(row[4]), prefix), set()).add(prefix + ' ' + canonical_id)
    for n in z.namelist():
        if not n.endswith('.xlsx') or 'overview' in n:
            continue
        w = openpyxl.load_workbook(io.BytesIO(z.read(n)), read_only=True, data_only=True)
        study = Path(n).stem
        for sh in w.sheetnames:
            if 'experimentresults' not in sh.replace('_', '').lower():
                continue
            vv = list(w[sh].iter_rows(min_row=6, max_row=1000, values_only=True))
            keys = list(vv[0])
            col = keys.index('BACTERIAL_STRAIN_NAME')
            labels = set((str(row[col]) for row in vv[1:] if row[col]))
            for prefix in ['KLEPN', 'PSEAE']:
                ids = study_map.get((study, prefix), set())
                observed = [lab for lab in labels if lab.startswith(prefix)]
                if len(ids) == 1 and len(observed) == 1:
                    key = norm(observed[0])
                    cid = next(iter(ids))
                    if key not in alias:
                        alias[key] = cid

    def canonical(v):
        return alias.get(norm(v), re.sub('\\s+', ' ', v).strip())
    save(WORK / 'ASSAY_STRAIN_ALIASES.json', alias)
    audit = {'excluded': {}, 'files': []}

    def exc(reason):
        audit['excluded'][reason] = audit['excluded'].get(reason, 0) + 1
    for n in z.namelist():
        if not n.endswith('.xlsx'):
            continue
        w = openpyxl.load_workbook(io.BytesIO(z.read(n)), read_only=True, data_only=True)
        sheets = [s for s in w.sheetnames if 'experimentresults' in s.replace('_', '').lower()]
        if not sheets:
            exc('workbook lacks result sheet')
            continue
        keys = None
        v = []
        for sheet in sheets:
            vv = list(w[sheet].iter_rows(min_row=6, max_row=2000, values_only=True))
            kk = list(vv[0])
            if keys is None:
                keys = kk + ['_sheet', '_source_row']
                v = [keys]
            for j, row in enumerate(vv[1:], start=7):
                obj = dict(zip(kk, row))
                v.append([obj.get(k) for k in keys[:-2]] + [sheet, j])
        rs = []
        for j, row in enumerate(v[1:], start=7):
            d = {k: v for k, v in zip(keys, row) if k}
            j = int(d['_source_row'])
            value = d.get('RESULT_VALUE')
            t = d.get('RELATIVE_TIMEPOINT')
            unit = str(d.get('RESULT_UNIT', ''))
            if value is None:
                continue
            if not isinstance(value, (int, float)):
                exc('non-numeric result')
                continue
            if 'CFU' not in str(d.get('EXPERIMENT_TYPE', '')) or 'log' not in unit.lower() or 'lung' not in unit.lower():
                exc('other assay or unit')
                continue
            if str(d.get('CPD_ID', '')).strip().lower() not in ['no compound treatment', 'no treatment', '#na (not applicable)']:
                exc('not explicit untreated control')
                continue
            if not isinstance(t, (int, float)):
                exc('non-numeric actual time, including early-death censoring')
                continue
            if str(d.get('RESULT_STATUS', '')).strip() != 'V (valid)':
                exc('not author-marked valid')
                continue
            if str(d.get('RESULT_OPERATOR')).strip() != '=':
                exc('non-equality/censored operator')
                continue
            if t < 0 or t > 24:
                exc('outside fixed 0–24 h window')
                continue
            rs.append((j, d))
        initial = {}
        for j, d in rs:
            strain = canonical(str(d.get('BACTERIAL_STRAIN_NAME')))
            if d['RELATIVE_TIMEPOINT'] == 0:
                initial.setdefault(strain, []).append(float(d['RESULT_VALUE']))
        initial = {k: float(np.mean(v)) for k, v in initial.items()}
        for j, d in rs:
            if d['RELATIVE_TIMEPOINT'] <= 0:
                continue
            strain = canonical(str(d.get('BACTERIAL_STRAIN_NAME')))
            provided_site = str(d.get('SITE'))
            site = Path(n).parts[1]
            if strain not in initial:
                exc('strain-study lacks time-zero calibration')
                continue
            rows.append(dict(group=site, study=n, site=site, time_h=float(d['RELATIVE_TIMEPOINT']), initial_logCFU=initial[strain], target=float(d['RESULT_VALUE']), anchor=f'standard_model_data_V1.0.zip:{n}:{d['_sheet']}:row{j}', source_strain_label=strain, provided_site=provided_site))
        audit['files'].append({'path': n, 'eligible_rows': len(rs)})
    save(WORK / 'ASSAY_PARSER_COUNTS.json', audit)
    output(78, rows, common('Untreated bacterial burden in total lung', 'log10 CFU / total lung', {'time_h': 'h; numeric actual time only', 'initial_logCFU': 'log10 CFU / total lung; mean observed time-zero cohort', 'site': 'source laboratory label'}, 'DSM/site-reference strain aliases resolved from source RefToDict plus explicit single-strain-study Overview links (source labeling discrepancies retained) and kept together. All ExperimentResults sheets included. Explicit untreated CFU lung single-value observations only, equality operator, compatible log-CFU lung units, numeric actual times 0–24 h. Time-zero animals form an explicitly allowed cohort calibration, not the same later animals. Non-numeric early-death times and censoring cannot be interpreted as exact scheduled times; exclusions are counted, and this creates survivorship/measurement selection limits. Source already reports virulence/reproducibility criteria; no new clinical efficacy claim.', 'whole source-directory laboratory/site', 'Retrospective whole-laboratory transfer; DSM and SITE labels remain partially inconsistent. Earlier invalidated fits used some later GSK outcomes, so no fresh confirmation. No strain-transfer, clinical safety or antibiotic efficacy claim.', 'Initial cohort burden and time/site only. No post-baseline measured target is an input; study/strain IDs are anchors, not predictors.'), ['GSK'])

def case86():
    d = pd.read_csv(src(86) / 'raw/EFP_long.csv')
    rows = []
    starts = {}
    for g, sub in d.groupby('batch_id', sort=False):
        sub = sub.sort_values('hh').copy()
        starts[str(g)] = str(sub.iloc[0]['date'])
        t = sub.hh.to_numpy(float)
        y = sub.hx.to_numpy(float)
        for j in range(6, len(sub) - 6):
            if t[j] - t[j - 6] != 6 or t[j + 6] - t[j] != 6 or (not np.isfinite([y[j], y[j - 6], y[j + 6]]).all()):
                continue
            rows.append(dict(group=str(g), time_h=t[j], current=y[j], slope6=(y[j] - y[j - 6]) / 6, target=y[j + 6], anchor=f'EFP_long.csv:row{sub.index[j] + 2}:future_row{sub.index[j + 6] + 2}'))
    reserved = sorted(starts, key=lambda g: pd.to_datetime(starts[g]))[-81:]
    sp = common('Chemical potency six hours ahead', 'source potency unit (undocumented)', {'time_h': 'h since cultivation, source hh', 'current': 'source potency unit; last available potency measurement', 'slope6': 'source potency unit/h from strictly past 6 h'}, 'Native hx is the source-loader target. Other undocumented abbreviations are excluded. Source units are not asserted to be mg/L or activity U/mL. 406 independent production batches; rows with exact 6 h lag/horizon only. No target smoothing or imputation. This is a six-hour prediction conditional on an available current potency assay, not an inline soft sensor.', 'whole production batch; chronologically latest 81 reserved', 'One industrial facility and one year; historical operational forecasting, no mechanistic law from unmapped sensors. Earlier batches only train later validation blocks.', 'Strictly causal potency history and cultivation clock. Matching plus/minus 6 h uses source clock; future values only become targets.')
    sp['cv'] = 'forward_batches'
    sp['chronological_group_order'] = sorted(starts, key=lambda g: pd.to_datetime(starts[g]))
    output(86, rows, sp, reserved)

def case96():
    z = zipfile.ZipFile(next((src(96) / 'raw').glob('*.zip')))
    rows = []
    for n in z.namelist():
        if not n.endswith('.txt'):
            continue
        d = pd.read_csv(io.BytesIO(z.read(n)))
        d['_row'] = np.arange(len(d)) + 2
        video = n.split('/')[-1].split('.MP4')[0]
        frames = {int(k): v for k, v in d.groupby('Frame_ID')}
        indexed = {(str(v), int(f)): r for v, f, r in zip(d.Vehicle_ID, d.Frame_ID, d.to_dict('records'))}
        for frame, sub in frames.items():
            if frame % 25:
                continue
            for _, r in sub.iterrows():
                vid = str(r.Vehicle_ID)
                future = indexed.get((vid, frame + 25))
                past = indexed.get((vid, frame - 25))
                if future is None or past is None:
                    continue
                other = sub[sub.Vehicle_ID != vid]
                angles = np.mod(other.Polar_X.to_numpy() - float(r.Polar_X), 2 * np.pi)
                k = int(np.argmin(angles))
                leader = other.iloc[k]
                gap = float(angles[k] * r.Polar_Y)
                rel = float(leader.v_Vel - r.v_Vel)
                if not np.isfinite([r.v_Vel, future['v_Vel'], past['v_Vel'], gap, rel, r.Polar_Y]).all():
                    continue
                rows.append(dict(group=video, sequence=n, speed=float(r.v_Vel), past_acc=float(r.v_Vel - past['v_Vel']), gap=gap, relative_speed=rel, radius=float(r.Polar_Y), lateral_gap=float(abs(leader.Polar_Y - r.Polar_Y)), count=len(sub), target=float(future['v_Vel']), anchor=f'TRAJECTORIES.zip:{n}:row{int(r._row)}:future_row{future['_row']}'))
    groups = sorted(set((r['group'] for r in rows)))
    sp = common('Author-extracted cyclist speed one second ahead', 'm/s', {'speed': 'm/s at current native frame', 'past_acc': 'm/s^2 from native speed 1 s earlier', 'gap': 'm; positive-angle arc gap to nearest forward angular bicycle', 'relative_speed': 'm/s; leader minus follower', 'radius': 'm', 'lateral_gap': 'm; radial separation to angular leader', 'count': 'tracked bicycles in frame'}, 'Source computer-vision/Kalman trajectories, 25 Hz; select every 25th frame and exact +/-25-frame pairs. Parts of the same original video remain together. Track IDs may be ambiguous; all 28 riders recur across videos. Source preprocessing may use future smoothing, so predictions are retrospective trajectory dynamics and not certified online safety. Angular-neighbor interaction is a testable approximation; lateral separation and direction reversal are falsifiers.', 'whole original video, all parts/participants', 'One controlled circular-track session, recurring riders; no new-rider, on-road safety or crash-prevention transfer claim.', 'Only current and past extracted speeds and current geometry/neighbor state. Future target speed is inaccessible to candidate replay.')
    output(96, rows, sp, groups[-2:])
