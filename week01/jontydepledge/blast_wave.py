import numpy as np
import matplotlib.pyplot as plt

# Parameters used to create data

rho = 1.2
C = 1.0
true_energy = 50.0

# use a fixed seed
rng = np.random.default_rng(12)

# Choose time values
t = np.linspace(0.5, 10.0, 12)

# Calculate model values
true_radius = C * (true_energy * t**2 / rho) ** (1 / 5)

# Add noise
noise = rng.normal(loc=0.0, scale=0.1, size=len(t))
measured_radius = true_radius + noise

# Fit log(R) against log(t)
log_t = np.log(t)
log_R = np.log(measured_radius)


# fit linear model
slope, intercept = np.polyfit(log_t, log_R, 1)

# Since
# intercept = log(C) + (1/5) log(E/rho),
# rearranging gives:
estimated_energy = rho * np.exp(5 * (intercept - np.log(C)))

fitted_log_R = slope * log_t + intercept
fitted_radius = np.exp(fitted_log_R)


# Print fitted results
print(f"Recovered slope: {slope:.4f}")
print(f"Recovered energy: {estimated_energy:.4f}")

percentage_error = (
    abs(estimated_energy - true_energy) / true_energy * 100
)

print(f"Energy percentage error: {percentage_error:.2f}%")



# Create figure
plt.figure(figsize=(7, 5))

plt.scatter(t, measured_radius, label="Synthetic measurements")

plt.plot(t, fitted_radius, label=f"Fitted line, slope = {slope:.3f}")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Time, t")
plt.ylabel("Blast radius, R")
plt.title("Taylor blast-wave scaling")
plt.legend()

# Save figure
plt.savefig("figure.png")
plt.show()