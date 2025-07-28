import argparse
from polyglot import make_book

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pgn', required=True)
    parser.add_argument('--engine', required=True)
    parser.add_argument('--depth', type=int, default=15)
    parser.add_argument('--output', default='book.bin')
    args = parser.parse_args()

    make_book(
        pgn=args.pgn,
        bin=args.output,
        depth=args.depth,
        engine=args.engine
    )
    print(f"Generated {args.output}")

if __name__ == '__main__':
    main()
