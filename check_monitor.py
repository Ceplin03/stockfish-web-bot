import mss

with mss.mss() as sct:
    for i, m in enumerate(sct.monitors):
        print(f"Monitor {i}: {m}")
