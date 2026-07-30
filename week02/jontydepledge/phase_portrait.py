import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

beta_values = [0, 1, 3]

ICs = [
    [-1, 1.5],
    [-2, -1],
    [2, -1.5],
]

t_span = (0, 4)
t_eval = np.linspace(*t_span, 1000)

for beta in beta_values:

    def system(t, z):
        theta, v = z
        return [v, -beta*v - np.sin(theta)]

    theta = np.linspace(-2*np.pi, 2*np.pi, 100)
    v = np.linspace(-3, 3, 100)
    Theta, V = np.meshgrid(theta, v)

    U = V
    W = -beta*V - np.sin(Theta)

    plt.figure()
    plt.streamplot(Theta, V, U, W, density=1.2)

    for ic in ICs:
        sol = solve_ivp(system, t_span, ic, t_eval=t_eval)
        plt.plot(sol.y[0], sol.y[1])

    plt.scatter([-2*np.pi, 0, 2*np.pi], [0, 0, 0])
    plt.scatter([-np.pi, np.pi], [0, 0], marker="x")

    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$\theta'$")
    plt.title(fr"$\beta={beta}$")
    plt.grid()
    plt.savefig(
        f"phase_portrait_beta_{beta}.png",
        dpi=300
    )
    plt.show()
