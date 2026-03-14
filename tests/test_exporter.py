import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.exporter import DialogueExporter
from core.extractor import DialogueExtractor

game_path = "Game_dummy/game"

extractor = DialogueExtractor(game_path)
dialogues = extractor.extract_all()

exporter = DialogueExporter()

output_file = "translation_project.json"

exporter.export_to_json(dialogues, output_file)
