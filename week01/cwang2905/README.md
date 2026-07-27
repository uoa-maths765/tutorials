# Taylor Blast-Wave Fit

Synthetic-data test of Taylor's blast-wave scaling law

    R(t) = C * (E t^2 / rho)^(1/5)

fit on log-log axes to recover the energy `E` from noisy "photographic"
radius measurements.


## Regenerating the figures

Run file `tut1.m` in MATLAB to

- generate 12 synthetic `(t, R)` measurements with noise,
- fit `log R` vs `log t` with `polyfit` ,
- plot fitted line and synthetic data points
- print the fitted slope, recovered `E` to the console,

The random seed is fixed (`rng(1)`) so the output is reproducible. Noise level can be altered.
