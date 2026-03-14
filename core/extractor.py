"""
Dialogue extraction engine

Responsible for scanning a Ren'Py game folder and extracting
all dialogue from every .rpy script.
"""

from core.parser import RenpyParser
from core.scanner import ScriptScanner


class DialogueExtractor:
    def __init__(self, game_path):
        self.game_path = game_path
        self.scanner = ScriptScanner(game_path)
        self.parser = RenpyParser()

    def extract_all(self):
        all_dialogues = []

        # scan semua file .rpy
        rpy_files = self.scanner.scan()

        for filepath in rpy_files:
            dialogues = self.parser.parse_file(filepath)
            all_dialogues.extend(dialogues)

        return all_dialogues
