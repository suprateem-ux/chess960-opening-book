import subprocess, sys

depth = 15
fens = "fens.txt"
output = "book.bin"
engine = "stockfish/stockfish-ubuntu-x86-64-bmi2"

cmd = [
    "./polyglot", "make-book",
    "-fen", fens,
    "-bin", output,
    "-max-ply", str(depth * 2),
    "-engine", engine
]

print("Running:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("Error:", res.stderr)
    sys.exit(res.returncode)

size = subprocess.check_output(["stat", "-c%s", output]).decode().strip()
size = int(size)
print(f"Book size: {size} bytes")
if size % 16 != 0:
    print("Invalid book.bin: size not divisible by 16")
    sys.exit(1)

print("✅ book.bin is valid and ready")
