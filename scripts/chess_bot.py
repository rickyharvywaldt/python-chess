import chess
import chess.pgn
import chess.engine
import yaml
import random

BOARD_FILE = "board.yaml"

# Load current board state
with open(BOARD_FILE, "r") as f:
    board_data = yaml.safe_load(f)

# Initialize chess board
fen = board_data.get("fen", "startpos")
board = chess.Board(fen if fen != "startpos" else None)

# Check if game is already over
if board_data.get("game_over"):
    print("Game over! Reset the board to start a new game.")
    exit(0)

# Select a move
legal_moves = list(board.legal_moves)
if not legal_moves:
    print("No legal moves available.")
    board_data["game_over"] = True
    board_data["winner"] = "draw"
else:
    # Pick a random legal move
    move = random.choice(legal_moves)
    board.push(move)
    board_data["moves"].append(move.uci())
    board_data["fen"] = board.fen()

    # Check for checkmate or stalemate
    if board.is_checkmate():
        board_data["game_over"] = True
        board_data["winner"] = "bot"
    elif board.is_stalemate() or board.is_insufficient_material():
        board_data["game_over"] = True
        board_data["winner"] = "draw"

# Save updated board
with open(BOARD_FILE, "w") as f:
    yaml.safe_dump(board_data, f)

print(f"Bot move: {move.uci()}")

