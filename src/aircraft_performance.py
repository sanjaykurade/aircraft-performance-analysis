"""
Aircraft Performance Analysis

Educational computational model for basic aircraft
performance analysis using Python.
"""

import numpy as np
import matplotlib.pyplot as plt


# Aircraft parameters
MASS = 1200.0
WING_AREA = 16.2
ASPECT_RATIO = 8.5
OSWALD_EFFICIENCY = 0.80
CD0 = 0.025
CL_MAX = 1.60
THRUST = 3500.0
RHO = 1.225
G = 9.80665


# Aircraft weight
WEIGHT = MASS * G


# Induced drag factor
K = 1 / (
    np.pi * OSWALD_EFFICIENCY * ASPECT_RATIO
)


# Estimated stall speed
STALL_SPEED = np.sqrt(
    (2 * WEIGHT)
    / (RHO * WING_AREA * CL_MAX)
)


# Thrust-to-weight ratio
THRUST_TO_WEIGHT = THRUST / WEIGHT


# Airspeed range
speed = np.linspace(20, 150, 300)


# Dynamic pressure
dynamic_pressure = 0.5 * RHO * speed**2


# Lift coefficient
lift_coefficient = WEIGHT / (
    dynamic_pressure * WING_AREA
)


# Drag coefficient
drag_coefficient = (
    CD0 + K * lift_coefficient**2
)


# Lift
lift = (
    dynamic_pressure
    * WING_AREA
    * lift_coefficient
)


# Drag
drag = (
    dynamic_pressure
    * WING_AREA
    * drag_coefficient
)


# Lift-to-drag ratio
lift_to_drag = lift / drag


# Simplified rate of climb
rate_of_climb = (
    (THRUST - drag) * speed
) / WEIGHT


# Display key results
print("=" * 60)
print("AIRCRAFT PERFORMANCE ANALYSIS")
print("=" * 60)

print(f"Aircraft mass          : {MASS:.1f} kg")
print(f"Aircraft weight        : {WEIGHT:.2f} N")
print(f"Induced drag factor k  : {K:.6f}")

print(
    f"Estimated stall speed  : "
    f"{STALL_SPEED:.2f} m/s"
)

print(
    f"Stall speed            : "
    f"{STALL_SPEED * 3.6:.2f} km/h"
)

print(
    f"Thrust-to-weight ratio : "
    f"{THRUST_TO_WEIGHT:.3f}"
)

print("=" * 60)


# Lift vs airspeed
plt.figure(figsize=(8, 5))
plt.plot(speed, lift)
plt.xlabel("Airspeed (m/s)")
plt.ylabel("Lift (N)")
plt.title("Lift vs Airspeed")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/figures/lift_vs_airspeed.png",
    dpi=300
)

plt.show()


# Drag vs airspeed
plt.figure(figsize=(8, 5))
plt.plot(speed, drag)
plt.xlabel("Airspeed (m/s)")
plt.ylabel("Drag (N)")
plt.title("Drag vs Airspeed")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/figures/drag_vs_airspeed.png",
    dpi=300
)

plt.show()


# Lift-to-drag ratio
plt.figure(figsize=(8, 5))
plt.plot(speed, lift_to_drag)
plt.xlabel("Airspeed (m/s)")
plt.ylabel("Lift-to-Drag Ratio (L/D)")
plt.title("Lift-to-Drag Ratio vs Airspeed")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/figures/lift_to_drag_vs_airspeed.png",
    dpi=300
)

plt.show()


# Rate of climb
plt.figure(figsize=(8, 5))
plt.plot(speed, rate_of_climb)
plt.axhline(0, linestyle="--")
plt.xlabel("Airspeed (m/s)")
plt.ylabel("Rate of Climb (m/s)")
plt.title("Simplified Rate of Climb vs Airspeed")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/figures/rate_of_climb_vs_airspeed.png",
    dpi=300
)

plt.show()
