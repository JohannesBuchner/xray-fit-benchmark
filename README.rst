Performance test case for x-ray spectral fitting
-------------------------------------------------

see generate.py (for sherpa)

see generatexspec.py (for xspec)

Benchmark
-------------

How fast is fitting if only the normalisations are varied?

This should be trivially fast (<10ms), as it is only matrix-vector multiplication,
and the poisson formula.

Model setup
-------------

* 3 spectra (Chandra + 2x NuSTAR)
* model
	* sum of 8 apecs
	* table models (download from https://zenodo.org/record/1169181)
* statistic: Poisson (cstat)
* backgrounds
    * in sherpa: model set (powerlaw)
    * in xspec: no model (WStat)



Current results
---------------

Sherpa:

* 14.89 model evaluations per second
* 21 model evaluations per second with scale1d

Xspec:

* 2 model evaluations per second
