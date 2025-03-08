import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Definizione dei parametri fisici
g = 9.81  # accelerazione gravitazionale (m/s^2)
L = 1.0   # lunghezza del pendolo (m)
theta0 = np.radians(30)  # angolo iniziale in radianti (30°)
omega0 = 0.0  # velocità angolare iniziale

# Intervallo di tempo
t_min, t_max = 0, 10  # Simuliamo per 10 secondi
t_eval = np.linspace(t_min, t_max, 200)  # 200 frame per l'animazione

# Definizione delle equazioni del moto
def pendulum_equations(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Risoluzione numerica
sol = solve_ivp(pendulum_equations, [t_min, t_max], [theta0, omega0], t_eval=t_eval)

# Estrazione dei risultati
theta = sol.y[0]  # Angolo nel tempo

# Calcoliamo le coordinate (x, y) del pendolo
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Creazione della figura per l'animazione
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-L-0.2, L+0.2)
ax.set_ylim(-L-0.2, L+0.2)
ax.set_aspect('equal')
ax.set_title("Animazione del Pendolo Semplice")

# Disegno dell'asta e della massa del pendolo
line, = ax.plot([], [], 'o-', lw=3, markersize=8)
trace, = ax.plot([], [], 'r-', alpha=0.5)  # Traccia del moto

# Memorizziamo il percorso del pendolo
x_trace, y_trace = [], []

# Funzione di aggiornamento per l'animazione
def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])  # Asta del pendolo
    x_trace.append(x[frame])
    y_trace.append(y[frame])
    trace.set_data(x_trace, y_trace)  # Traccia del moto
    return line, trace

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=len(t_eval), interval=50, blit=True)

plt.show()
