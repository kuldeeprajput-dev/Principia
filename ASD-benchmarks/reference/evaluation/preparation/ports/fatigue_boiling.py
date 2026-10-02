"""Source-derived native parser; no fitting; historical code provenance in PORTS.json."""
from pathlib import Path
import sys, json, hashlib, re, zipfile, datetime, io, math, time, collections
import xml.etree.ElementTree as ET
import numpy as np, pandas as pd, openpyxl, scipy.io
CASES = ['24_materials_dtu_composite_fatigue', '27_fluid_dynamics_kth_boiling']

def saturation(p):
    lo, hi = (273.16, 647.095999)
    a = np.array([-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502])
    ap = np.array([1, 1.5, 3, 3.5, 4, 7.5])
    for _ in range(80):
        t = (lo + hi) / 2
        q = 1 - t / 647.096
        ps = 22064000 * np.exp(647.096 / t * np.sum(a * q ** ap))
        if ps < p:
            lo = t
        else:
            hi = t
    t = (lo + hi) / 2
    q = 1 - t / 647.096
    b = np.array([1.99274064, 1.09965342, -0.510839303, -1.75493479, -45.5170352, -674694.45])
    bp = np.array([1 / 3, 2 / 3, 5 / 3, 16 / 3, 43 / 3, 110 / 3])
    c = np.array([-2.0315024, -2.6830294, -5.38626492, -17.2991605, -44.7586581, -63.9201063])
    cp = np.array([1 / 3, 2 / 3, 4 / 3, 3, 37 / 6, 71 / 6])
    return (t, 322 * (1 + np.sum(b * q ** bp)), 322 * np.exp(np.sum(c * q ** cp)))
