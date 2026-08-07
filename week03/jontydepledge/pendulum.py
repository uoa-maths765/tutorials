import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from pathlib import Path

# Folder containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

def f_int(theta, theta0):
    return 4/np.sqrt(2 * np.cos(theta) - 2 * np.cos(theta0))


def T(theta0):
    return quad(f_int, 0, theta0, args=(theta0))[0]


theta_values = np.arange(0.01, 3.14, 0.01)
period_exact = [T(theta0) for theta0 in theta_values]

period_linear = 2*np.pi* theta_values**0

period_better = 2*np.pi*(1+theta_values**2 / 16)

plt.plot(theta_values, period_exact, label="Exact")
plt.plot(theta_values, period_better, label="Quadratic")
plt.plot(theta_values, period_linear, label="Linear")

plt.title("Model Comparison")
plt.xlabel(r"$\theta_0$")
plt.ylabel("Period")
plt.legend()

plt.savefig(
    SCRIPT_DIR / "period_plot.png",
    dpi=300
)
print('test')