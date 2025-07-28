import chess.pgn
import chess.engine
import chess.polyglot
import struct

STOCKFISH_PATH = "stockfish/stockfish-ubuntu-x86-64-bmi2"
PGN_FILE = "chess960_book_3moves.pgn"
BIN_FILE = "book.bin"
MAX_DEPTH = 15

def polyglot_key(board):
    return chess.polyglot.zobrist_hash(board)

def write_entry(f, key, board, move, weight=1, learn=0):
    encoded_move = chess.polyglot.encode_move(board, move)
    encoded = struct.pack(">QHHI", key, encoded_move, weight, learn)
    f.write(encoded)

def build_book():
    seen = set()
    with open(PGN_FILE) as pgn, open(BIN_FILE, "wb") as bin_file, chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as sf:
        while game := chess.pgn.read_game(pgn):
            board = game.board()
            for move in game.mainline_moves():
                if board.fullmove_number * 2 > MAX_DEPTH:
                    break
                key = polyglot_key(board)
                if (key, move) not in seen:
                    seen.add((key, move))
                    write_entry(bin_file, key, board, move)
                board.push(move)
    print(f"✅ Finished writing {len(seen)} positions to {BIN_FILE}")

if __name__ == "__main__":
    build_book()
