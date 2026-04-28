DeepKnight Web ♟️DeepKnight Web adalah aplikasi catur berbasis web interaktif yang mengintegrasikan kecerdasan buatan (AI) dari Stockfish Engine ke dalam antarmuka modern. Project ini menggabungkan kekuatan Python (Flask) sebagai otak backend dan JavaScript sebagai wajah frontend untuk menciptakan pengalaman bermain catur yang mulus.!🚀 Fitur UnggulanAI Intelligence: Menggunakan Stockfish Engine terbaru untuk analisis langkah yang presisi.Interactive Interface: Fitur drag-and-drop yang responsif menggunakan chessboard.js.Move Highlighting: Penanda visual kuning untuk melacak langkah terakhir (asal dan tujuan), memudahkan pemain mengikuti strategi AI.Real-time Validation: Validasi aturan catur secara instan menggunakan chess.js di sisi klien.FEN Synchronization: Komunikasi backend-frontend yang stabil menggunakan Forsyth-Edwards Notation.📂 Struktur ProjectPlaintextchess_bot/
├── engine/                 # Folder berisi file executable Stockfish
│   └── stockfish.exe
├── templates/              # Folder untuk file UI (HTML)
│   └── index.html
├── static/                 # Folder asset (CSS, JS, Images)
├── server.py               # Backend Flask (Server Utama)
└── README.md
🛠️ Instalasi & Persiapan1. PrasyaratPastikan kamu sudah menginstal Python 3.10 ke atas dan memiliki engine Stockfish (versi Windows .exe).2. Instalasi LibraryJalankan perintah berikut di terminal:Bashpip install flask stockfish
3. Konfigurasi PathBuka file server.py dan sesuaikan lokasi file Stockfish kamu:PythonSTOCKFISH_PATH = r"C:\path\ke\folder\kamu\engine\stockfish.exe"
4. Menjalankan AplikasiJalankan server dengan perintah:Bashpython server.py
Setelah berjalan, buka browser dan akses http://127.0.0.1:5000.🖥️ Teknologi yang DigunakanBackend: Flask (Python)AI Engine: StockfishFrontend UI: Chessboard.jsLogic & Validation: Chess.js📸 Tampilan AplikasiBerikut adalah cuplikan tampilan antarmuka DeepKnight Web saat digunakan:FiturScreenshotGameplay!Highlighting!🤝 KontribusiProject ini bersifat open-source. Jika kamu ingin menambahkan fitur seperti suara, timer, atau mode multiplayer, silakan buat Pull Request atau buka Issue baru.Author: [Sepri Iratas]
