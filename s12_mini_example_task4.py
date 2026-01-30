import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def taylor_sin(x, x0, omega):
    f0 = np.sin(omega * x0)
    f1 = omega * np.cos(omega * x0)
    f2 = -omega**2 * np.sin(omega * x0)
    dx = x - x0
    return f0 + f1 * dx + 0.5 * f2 * dx**2

x = np.linspace(0.0, 2.0 * np.pi, 400)
x0_init = 0.5
omega_init = 2.0

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)

line_f, = ax.plot(x, np.sin(omega_init * x), label="sin(omega x)", linewidth=2)
line_t, = ax.plot(x, taylor_sin(x, x0_init, omega_init), label="Taylor", linestyle="--")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")

ax_x0 = fig.add_axes([0.2, 0.1, 0.65, 0.03])
ax_omega = fig.add_axes([0.2, 0.05, 0.65, 0.03])

slider_x0 = Slider(ax_x0, "x0", 0.0, 2.0 * np.pi, valinit=x0_init)
slider_omega = Slider(ax_omega, "omega", 0.1, 6.0, valinit=omega_init)

def update(_):
    x0 = slider_x0.val
    omega = slider_omega.val
    line_f.set_ydata(np.sin(omega * x))
    line_t.set_ydata(taylor_sin(x, x0, omega))
    fig.canvas.draw_idle()

slider_x0.on_changed(update)
slider_omega.on_changed(update)

plt.show()