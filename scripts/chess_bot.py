import chess
import yaml
import random

BOARD_FILE = "board.yaml"

# Load board
try:
    with open(BOARD_FILE, "r") as f:
        board_data = yaml.safe_load(f)
except FileNotFoundError:
    # Create initial board if missing
    board_data = {"fen": None, "moves": [], "game_over": False, "winner": None}

# Initialize board
fen = board_data.get("fen")
if fen is None or fen == "startpos":
    board = chess.Board()  # start position
else:
    board = chess.Board(fen)

# If game is over, mark it
if board.is_game_over():
    board_data["game_over"] = True
    result = board.result()  # "1-0", "0-1", "1/2-1/2"
    if result == "1-0":
        board_data["winner"] = "white"
    elif result == "0-1":
        board_data["winner"] = "black"
    else:
        board_data["winner"] = "draw"
    print("Game over! Result:", result)
else:
    # Generate bot move (~1100 Elo via random legal move)
    legal_moves = list(board.legal_moves)
    if legal_moves:
        move = random.choice(legal_moves)
        board.push(move)
        board_data["moves"].append(move.uci())
        board_data["fen"] = board.fen()
        print(f"Bot move: {move.uci()}")
    else:
        print("No legal moves available, game over.")
        board_data["game_over"] = True

# Save updated board
with open(BOARD_FILE, "w") as f:
    yaml.safe_dump(board_data, f)

