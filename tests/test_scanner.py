import os
import sys

# tambahkan root project ke python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.scanner import ScriptScanner

game_path = "Game_dummy/game"

scanner = ScriptScanner(game_path)
files = scanner.scan()

print("Files found:")

for f in files:
    print(f)
