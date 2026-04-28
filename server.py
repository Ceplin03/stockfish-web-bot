from flask import Flask, render_template, request, jsonify
from stockfish import Stockfish

app = Flask(__name__)

# Inisialisasi Stockfish
STOCKFISH_PATH = r"C:\laragon\www\chess_bot\engine\stockfish-windows-x86-64.exe"
stockfish = Stockfish(path=STOCKFISH_PATH, depth=15)
stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_white_move', methods=['POST'])
def get_white_move():
    data = request.json
    fen = data.get('fen') # Ambil posisi papan secara keseluruhan (FEN)

    # Sinkronkan papan Stockfish dengan posisi dari web
    stockfish.set_fen_position(fen)

    # Dapatkan langkah terbaik putih dari posisi tersebut
    putih_move = stockfish.get_best_move()

    # Kirim langkah putih ke web
    return jsonify({"move": putih_move})

if __name__ == '__main__':
    app.run(debug=True, port=5000)