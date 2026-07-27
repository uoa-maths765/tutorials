# Report

Using synthetic data generated from Taylor's blast-wave model,

    R = (Et^2/rho)^(1/5)

with rho = 1.2 and E = 1000, a linear regression was performed on

    log(R) versus log(t).

## Results

Recovered slope:

    0.3996

Theoretical slope:

    0.400

Recovered energy:

    981.35

True energy:

    1000

Slope error:

    0.09%

Energy error:

    1.86%

## Discussion

The recovered slope is close to the theoretical value 2/5.

The energy estimate is obtained from the intercept. Since the
intercept appears inside an exponential transformation,

    E = rho exp(5a),

small errors in the intercept become amplified when estimating E.
Consequently the energy estimate is generally less accurate than the
slope estimate.

An interesting result is that the slope can be extremely accurate while
the energy estimate still has a noticeable error. This happens because
the slope depends on the trend of all data points, whereas the energy
depends on the intercept, which is more sensitive to measurement noise.

## Conclusion

The log-log representation successfully recovers the expected power-law
relationship R ∝ t^(2/5). The slope estimate is typically more accurate
and robust than the energy estimate, while the recovered energy remains
reasonably close to the true value.