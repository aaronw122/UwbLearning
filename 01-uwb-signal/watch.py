import time
from pathlib import Path

import matplotlib.pyplot as plt

TARGET = Path(__file__).parent / "index.py"


def render():
    """Re-execute index.py onto the current figure, skipping its blocking show()."""
    src = TARGET.read_text().replace("plt.show()", "")
    plt.clf()
    try:
        exec(compile(src, str(TARGET), "exec"), {"__name__": "__hot__"})
        plt.gcf().canvas.draw_idle()
    except Exception as e:  # keep the window alive on syntax/runtime errors
        print(f"error: {e}")


plt.ion()
render()
last = TARGET.stat().st_mtime
print(f"watching {TARGET.name} — edit + save to reload (Ctrl-C to quit)")

while plt.get_fignums():  # stop when you close the window
    plt.pause(0.3)
    m = TARGET.stat().st_mtime
    if m != last:
        last = m
        print("reloading...")
        render()
