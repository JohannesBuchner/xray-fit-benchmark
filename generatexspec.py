import tqdm
import numpy as np
import xspec

s1 = xspec.Spectrum('cdfs4Ms_179_bkg.pi')
s2 = xspec.Spectrum('bgd_60arcsec.pha')
s3 = xspec.Spectrum('bgd_60arcsec.pha')
s1.ignore('1:**-0.3')
s1.ignore('1:8.0-**')
s2.ignore('2:**-3.0')
s2.ignore('2:77.0-**')
s3.ignore('3:**-3.0')
s3.ignore('3:77.0-**')
xspec.Fit.statMethod = 'cstat'

m = xspec.Model('tbabs * (apec + apec + apec + apec + apec + apec + apec + atable{../specmodels/uxclumpy-cutoff.fits} + atable{../specmodels/uxclumpy-cutoff-omni.fits})')

m.TBabs.nH = 1.0
m.apec.kT = 0.1 
m.apec_3.kT = 0.2
m.apec_4.kT = 0.3
m.apec_5.kT = 0.4
m.apec_6.kT = 0.5
m.apec_7.kT = 0.6
m.apec_8.kT = 0.7

def reset_norms(factor = 1):
	for ai in m.apec, m.apec_3, m.apec_4, m.apec_5, m.apec_6, m.apec_7, m.apec_8:
		ai.norm = np.random.uniform(0, factor)
	m.torus.norm = np.random.uniform(0, factor)
	m.scat.norm = np.random.uniform(0, factor)
	return xspec.Fit.statistic

for i in tqdm.trange(1000):
	xspec.Xset.chatter, xspec.Xset.logChatter = 0, 0
	reset_norms(1e-7)
