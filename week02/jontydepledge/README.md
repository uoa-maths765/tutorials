# Week 2 Tutorial – Phase Portraits

This script generates phase portraits for the damped pendulum system

$
\theta' = v, \qquad
v' = -\beta v - \sin(\theta),
$

for the three parameter values $\beta = 0, 1, 3$.

For each value of $\beta$, the script:
- plots the phase portrait
- computes several representative trajectories
- marks the equilibrium points
- saves the resulting figure

## Requirements

- Python 3
- NumPy
- Matplotlib
- SciPy

## Running

Run the script with

```bash
python phase_portrait.py