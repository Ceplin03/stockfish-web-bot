import cv2
import numpy as np
import mss

SCRCPY_X = 0
SCRCPY_Y = 0
SCRCPY_W = 480
SCRCPY_H = 960

with mss.mss() as sct:
    monitor = {
        "left": SCRCPY_X,
        "top": SCRCPY_Y,
        "width": SCRCPY_W,
        "height": SCRCPY_H
    }
    img = np.array(sct.grab(monitor))

frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

points = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print("Klik:", x, y)

cv2.imshow("SCRCPY - Klik kiri atas & kanan bawah papan", frame)
cv2.setMouseCallback("SCRCPY - Klik kiri atas & kanan bawah papan", mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(points) != 2:
    raise Exception("WAJIB klik 2 titik papan")

BOARD_TOP_LEFT = points[0]
BOARD_BOTTOM_RIGHT = points[1]

with open("board_config.txt", "w") as f:
    f.write(f"{BOARD_TOP_LEFT[0]},{BOARD_TOP_LEFT[1]}\n")
    f.write(f"{BOARD_BOTTOM_RIGHT[0]},{BOARD_BOTTOM_RIGHT[1]}\n")

print("Koordinat papan disimpan ke board_config.txt")

# ==== VALIDASI GRID ====
x1, y1 = BOARD_TOP_LEFT
x2, y2 = BOARD_BOTTOM_RIGHT
board = frame[y1:y2, x1:x2]

h, w, _ = board.shape
ch = h // 8
cw = w // 8

for r in range(8):
    for c in range(8):
        cv2.rectangle(
            board,
            (c*cw, r*ch),
            ((c+1)*cw, (r+1)*ch),
            (0,255,0),
            1
        )

cv2.imshow("BOARD GRID VALIDATION", board)
cv2.waitKey(0)
cv2.destroyAllWindows()
