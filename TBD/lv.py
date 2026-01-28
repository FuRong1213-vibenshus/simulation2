"""
lotka_volterra.py

En simpel Lotka–Volterra (predator-prey) model til undervisning.

Model (klassisk form):
    dP/dt = a*P - b*P*Q
    dQ/dt = -c*Q + d*P*Q

Hvor:
    P = prey (byttedyr)
    Q = predator (rovdyr)
    a = prey fødselsrate
    b = prædation (kontakt rate)
    c = predator død (dødsrate)
    d = predator reproduktionsrate pr. spist prey

Dette script indeholder:
- RK4 integrator
- funktioner til simulering, plotting og gemning af data
- vejledende parametre og eksempler
"""

import csv
from dataclasses import dataclass
from typing import Tuple, List
import numpy as np
import matplotlib.pyplot as plt


# -------------------------
# Model-parametre container
# -------------------------
@dataclass
class LVParams:
    a: float  # prey fødselsrate
    b: float  # prædation (kontakt)
    c: float  # predator død
    d: float  # predator reproduktion per spist prey


# -------------------------
# Højreside (RHS) af ODE
# -------------------------
def lv_rhs(state: np.ndarray, params: LVParams) -> np.ndarray:
    """
    state: array([P, Q])
    returnerer dstate/dt: array([dP/dt, dQ/dt])
    """
    P, Q = state
    dP = params.a * P - params.b * P * Q
    dQ = -params.c * Q + params.d * P * Q
    return np.array([dP, dQ], dtype=float)


# -------------------------
# RK4 integrator (fix tidsteg)
# -------------------------
def rk4_integrate(rhs, state0: np.ndarray, t0: float, t1: float, dt: float, params) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrer ODE-systemet med RK4 fra t0 til t1 med step dt.
    Returnerer (t_array, states_array) hvor states_array.shape == (Nsteps, 2)
    """
    steps = int(np.ceil((t1 - t0) / dt))
    t = np.linspace(t0, t0 + steps * dt, steps + 1)
    states = np.zeros((steps + 1, state0.size), dtype=float)
    states[0] = state0.astype(float)

    s = state0.copy()
    for i in range(steps):
        k1 = rhs(s, params)
        k2 = rhs(s + 0.5 * dt * k1, params)
        k3 = rhs(s + 0.5 * dt * k2, params)
        k4 = rhs(s + dt * k3, params)
        s = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        # sørg for ikke-negative populationer (numerisk)
        s = np.maximum(s, 0.0)
        states[i + 1] = s

    return t, states


# -------------------------
# Hjælpefunktioner: simulér og plot
# -------------------------
def simulate_lv(params: LVParams,
                P0: float,
                Q0: float,
                t0: float = 0.0,
                t1: float = 50.0,
                dt: float = 0.01) -> Tuple[np.ndarray, np.ndarray]:
    """Kør en simulation og returnér t og states"""
    state0 = np.array([P0, Q0], dtype=float)
    t, states = rk4_integrate(lv_rhs, state0, t0, t1, dt, params)
    return t, states


def plot_time_series(t: np.ndarray, states: np.ndarray, title: str = "Lotka–Volterra"):
    prey = states[:, 0]
    pred = states[:, 1]
    plt.figure(figsize=(8, 4.5))
    plt.plot(t, prey, label="Prey (P)")
    plt.plot(t, pred, label="Predator (Q)")
    plt.xlabel("Tid")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_phase(states: np.ndarray, title: str = "Faseplot (P vs Q)"):
    prey = states[:, 0]
    pred = states[:, 1]
    plt.figure(figsize=(6, 6))
    plt.plot(prey, pred, lw=1)
    plt.xlabel("Prey (P)")
    plt.ylabel("Predator (Q)")
    plt.title(title)
    # markér startpunkt
    plt.scatter(prey[0], pred[0], color="green", label="start")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# -------------------------
# Gem data til CSV (valgfrit)
# -------------------------
def save_to_csv(filename: str, t: np.ndarray, states: np.ndarray):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["t", "P", "Q"])
        for ti, s in zip(t, states):
            writer.writerow([ti, s[0], s[1]])
    print(f"Data gemt i {filename}")


# -------------------------
# Parameter-sweep (enkelt)
# -------------------------
def param_sweep(base_params: LVParams,
                vary_name: str,
                vary_values: List[float],
                P0: float,
                Q0: float,
                t1: float = 100.0,
                dt: float = 0.05):
    """
    Kør simulationer hvor én parameter varieres.
    Viser tidserier i samme plot for sammenligning.
    """
    plt.figure(figsize=(8, 5))
    for val in vary_values:
        p = LVParams(base_params.a, base_params.b, base_params.c, base_params.d)
        setattr(p, vary_name, val)
        t, states = simulate_lv(p, P0, Q0, t1=t1, dt=dt)
        prey = states[:, 0]
        plt.plot(t, prey, label=f"{vary_name}={val:.3g}")
    plt.xlabel("Tid")
    plt.ylabel("Prey (P)")
    plt.legend()
    plt.title(f"Sammenligning: effekt af '{vary_name}' på Prey population")
    plt.tight_layout()
    plt.show()


# -------------------------
# Eksempel & brug (kan ændres af elever)
# -------------------------
if __name__ == "__main__":
    # Baseline parametre (pædagogisk valgt)
    params = LVParams(a=1.1, b=0.1, c=1.5, d=0.075)

    # Startpopulationer
    P0 = 40.0
    Q0 = 9.0

    # Simuler og plot
    t, states = simulate_lv(params, P0, Q0, t1=80.0, dt=0.05)
    plot_time_series(t, states, title="Lotka–Volterra: tidserie")
    plot_phase(states, title="Lotka–Volterra: faseplot")

    save_to_csv("lv_baseline.csv", t, states)

    # Eksempel på parameter-sweep (kun Prey vist)
    param_sweep(params, "b", [0.05, 0.08, 0.1, 0.15], P0, Q0, t1=80.0, dt=0.1)
