import os
import sys

# tambahkan root project ke python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.parser import RenpyParser

# file dummy untuk test

test_file = "Game_dummy/game/script.rpy"

parser = RenpyParser()
dialogues = parser.parse_file(test_file)

print("Dialoges found:\n")

for d in dialogues:
    print(f"[{d.id}] {d.speaker}: {d.original_text}")
