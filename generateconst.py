import tqdm
import numpy as np
from sherpa.astro.ui import *

load_pha(1, 'cdfs4Ms_179_bkg.pi')
#load_bkg(1, 'cdfs4Ms_179_bkg.pi')
for i in 2, 3:
	load_pha(i, 'bgd_60arcsec.pha')
	#load_rmf(i, 'nustar.rmf')
	#load_arf(i, 'point_30arcsecRad_1arcminOA.arf')
	#load_bkg(i, 'bgd_60arcsec.pha')
	#load_bkg_rmf(i, 'nustar.rmf')
	#load_bkg_arf(i, 'point_30arcsecRad_1arcminOA.arf')
load_xstable_model('torus', '../specmodels/uxclumpy-cutoff.fits')
load_xstable_model('omni', '../specmodels/uxclumpy-cutoff-omni.fits') 
torus = get_model_component('torus')
omni = get_model_component('omni')
set_stat('cstat')
set_model(1, xstbabs.galabso * (scale1d.norm1 * xsapec.a1 + scale1d.norm2 * xsapec.a2 + scale1d.norm3 * xsapec.a3 + scale1d.norm4 * xsapec.a4 + scale1d.norm5 * xsapec.a5 + scale1d.norm6 * xsapec.a6 + scale1d.norm7 * xsapec.a7))
xstbabs.galabso.nH = 1.0
xsapec.a1.kT = 0.1 
xsapec.a2.kT = 0.2
xsapec.a3.kT = 0.3
xsapec.a4.kT = 0.4
xsapec.a5.kT = 0.5
xsapec.a6.kT = 0.6
xsapec.a7.kT = 0.7
mymodel = xstbabs.galabso * (scale1d.torusnorm * torus + scale1d.omninorm * omni)
set_model(2, mymodel)
set_model(3, mymodel)
xspowerlaw.pbkg.norm = 1e-8
xspowerlaw.pbkg.PhoIndex = 0
xspowerlaw.nupbkg.norm = 1e-5
xspowerlaw.nupbkg.PhoIndex = 0
set_bkg_model(1, xspowerlaw.pbkg)
set_bkg_model(2, xspowerlaw.nupbkg)
set_bkg_model(3, xspowerlaw.nupbkg)

def reset_norms(factor = 1):
	for ai in scale1d.norm1, scale1d.norm2, scale1d.norm3, scale1d.norm4, scale1d.norm5, scale1d.norm6, scale1d.norm7:
		ai.c0 = np.random.uniform(0, factor)
	scale1d.torusnorm.c0 = np.random.uniform(0, factor)
	scale1d.omninorm.c0 = np.random.uniform(0, factor)
	return calc_stat()

fake_pha(1, arf=get_arf(1), rmf=get_rmf(1), exposure=1e6, backscal=1, areascal=100, bkg=get_bkg(1))
fake_pha(2, arf=get_arf(2), rmf=get_rmf(2), exposure=50000, backscal=1, areascal=10, bkg=get_bkg(2))
fake_pha(3, arf=get_arf(3), rmf=get_rmf(3), exposure=50000, backscal=1, areascal=10, bkg=get_bkg(3))

ignore_id(1, None, 0.3)
ignore_id(1, 8, None)
ignore_id(2, None, 3)
ignore_id(2, 77, None)
ignore_id(3, None, 3)
ignore_id(3, 77, None)

for i in tqdm.trange(1000):
	reset_norms(1e-7)
