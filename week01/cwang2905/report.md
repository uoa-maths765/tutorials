# Report: Recovering Blast Energy from Synthetic Photographic Data

## Setup

Taylor's scaling law predicts

    R(t) = C (E t^2 / rho)^(1/5)

A synthetic data set was generated with `rho = 1.2`, `C = 1`, and a chosen
"true" energy `E_true = 100`, sampled at 12 evenly spaced times between
0.1 and 1. Each radius measurement was perturbed by additive
Gaussian noise.

`E` was then treated as unknown and recovered by fitting a straight line to
`log R` vs `log t`.

## Results

| Quantity | Value |
|---|---|
| Theoretical slope | 0.4000 |
| Fitted slope | 0.4040 |
| True Energy | 100.0000 |
| Recovered Energy | 99.2395 |


## Discussion

The error in slope and energy is small, indicating our theory is correct. This is probably due to limited noise. Next steps would be to increase noise and explore how this relates to the error in estimates.