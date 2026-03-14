import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.extractor import DialogueExtractor

game_path = "Game_dummy/game"

extractor = DialogueExtractor(game_path)

dialogues = extractor.extract_all()

print("\nAll Dialogues Found\n")

for d in dialogues:
    print(f"[{d.id}] {d.speaker}: {d.original_text}")
