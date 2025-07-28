import sys, chess.pgn

pgn_path = "chess960_book_3moves.pgn"
out = "fens.txt"
fens = set()

with open(pgn_path, encoding="utf8") as f:
    while True:
        game = chess.pgn.read_game(f)
        if game is None: break
        fen = game.headers.get("FEN")
        if fen:
            fens.add(fen.strip())

with open(out, "w") as fo:
    for fen in sorted(fens):
        fo.write(fen + "\n")

print(f"Wrote {len(fens)} unique FENs to {out}")
