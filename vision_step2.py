import cv2
import numpy as np
import mss
import time

SCRCPY_X = 0
SCRCPY_Y = 0
SCRCPY_W = 480
SCRCPY_H = 960

# ==== LOAD BOARD CONFIG ====
with open("board_config.txt") as f:
    x1, y1 = map(int, f.readline().split(","))
    x2, y2 = map(int, f.readline().split(","))

BOARD_TOP_LEFT = (x1, y1)
BOARD_BOTTOM_RIGHT = (x2, y2)

# ==== DETEKSI ADA BIDAK ====
def detect_occupancy(cell):
    gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return "x" if np.sum(edges > 0) > 300 else "."

# ==== CAPTURE BOARD ====
def capture_board():
    with mss.mss() as sct:
        monitor = {
            "left": SCRCPY_X,
            "top": SCRCPY_Y,
            "width": SCRCPY_W,
            "height": SCRCPY_H
        }
        img = np.array(sct.grab(monitor))

    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    board = frame[
        BOARD_TOP_LEFT[1]:BOARD_BOTTOM_RIGHT[1],
        BOARD_TOP_LEFT[0]:BOARD_BOTTOM_RIGHT[0]
    ]

    h, w, _ = board.shape
    ch = h // 8
    cw = w // 8

    matrix = []
    for r in range(8):
        row = []
        for c in range(8):
            cell = board[r*ch:(r+1)*ch, c*cw:(c+1)*cw]
            row.append(detect_occupancy(cell))
        matrix.append(row)

    return matrix

# ==== MATRIX DIFF → MOVE ====
def detect_move(prev, curr):
    from_sq = None
    to_sq = None

    for r in range(8):
        for c in range(8):
            if prev[r][c] == "x" and curr[r][c] == ".":
                from_sq = (r, c)
            elif prev[r][c] == "." and curr[r][c] == "x":
                to_sq = (r, c)

    if from_sq and to_sq:
        return index_to_square(from_sq) + index_to_square(to_sq)
    return None

def index_to_square(pos):
    r, c = pos
    return chr(ord('a') + c) + str(8 - r)

# ===============================
# MAIN LOOP (BLACK ONLY)
# ===============================
print("VISION STEP 2 — HITAM SAJA")
print("PUTIH harus jalan dulu (Stockfish / manusia)")
print("Program mulai mendeteksi SETELAH itu\n")

prev_board = capture_board()
WHITE_MOVE_SKIPPED = False

while True:
    time.sleep(1.6)  # tunggu animasi stabil
    curr_board = capture_board()

    move = detect_move(prev_board, curr_board)

    if move:
        if not WHITE_MOVE_SKIPPED:
            # langkah pertama pasti PUTIH → abaikan
            WHITE_MOVE_SKIPPED = True
            print("Langkah putih diabaikan:", move)
        else:
            # validasi sederhana langkah hitam
            if move[1] in "78" or move[3] in "56":
                print("Langkah HITAM:", move)
        prev_board = curr_board
    else:
        prev_board = curr_board
