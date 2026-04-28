import subprocess
import time
from stockfish import Stockfish

ADB_PATH = r"D:\scrcpy-win64-v3.3.4\adb.exe"
# Ubah baris ini
STOCKFISH_PATH = r"C:\laragon\www\chess_bot\engine\stockfish-windows-x86-64.exe"

# =====================
# INIT STOCKFISH
# =====================
stockfish = Stockfish(
    path=STOCKFISH_PATH,
    depth=15
)

# Posisi awal, PUTIH jalan dulu
stockfish.set_fen_position(
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
)

# =====================
# KOORDINAT PAPAN
# =====================
BOARD_TOP_LEFT = (120, 680)
BOARD_BOTTOM_RIGHT = (960, 1520)
SQUARE_SIZE = (BOARD_BOTTOM_RIGHT[0] - BOARD_TOP_LEFT[0]) // 8

def tap(x, y, delay=0.25):
    subprocess.run(
        [ADB_PATH, "shell", "input", "tap", str(int(x)), str(int(y))],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(delay)

def square_to_xy(square):
    file = ord(square[0]) - ord('a')
    rank = 8 - int(square[1])
    x = BOARD_TOP_LEFT[0] + file * SQUARE_SIZE + SQUARE_SIZE // 2
    y = BOARD_TOP_LEFT[1] + rank * SQUARE_SIZE + SQUARE_SIZE // 2
    return x, y

def play_move(move):
    f, t = move[:2], move[2:4]
    x1, y1 = square_to_xy(f)
    x2, y2 = square_to_xy(t)
    tap(x1, y1)
    tap(x2, y2)

# =====================
# GAME LOOP (BENAR)
# =====================
print("MODE: Stockfish PUTIH vs Bot HITAM")
print("Stockfish akan jalan pertama...\n")

# 1️⃣ PUTIH JALAN PERTAMA
first_move = stockfish.get_best_move()
print("Stockfish (putih):", first_move)
play_move(first_move)
stockfish.make_moves_from_current_position([first_move])

# 2️⃣ LOOP: INPUT HITAM → PUTIH BALAS
while True:
    hitam = input("\nMasukkan langkah HITAM (contoh: e7e5): ").strip()

    if not hitam:
        print("Langkah hitam kosong, ulangi.")
        continue

    # update posisi dengan langkah hitam
    stockfish.make_moves_from_current_position([hitam])

    # putih balas
    move = stockfish.get_best_move()
    print("Stockfish (putih):", move)
    play_move(move)
    stockfish.make_moves_from_current_position([move])
