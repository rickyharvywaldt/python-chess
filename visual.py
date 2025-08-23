import chess
import yaml

BOARD_FILE = "board.yaml"

with open(BOARD_FILE, "r") as f:
    board_data = yaml.safe_load(f)

fen = board_data.get("fen", "startpos")
board = chess.Board(fen if fen != "startpos" else None)

# Only push moves if FEN was the starting position
if fen == "startpos":
    for move in board_data.get("moves", []):
        board.push_uci(move)

print(board)
print("\nFEN:", board.fen())

