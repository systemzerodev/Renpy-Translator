"""
RenPy script parser

Responsible for reading .rpy files and extracting dialogue lines.
"""

import re

from core.models import DialogueEntry


class RenpyParser:
    def __init__(self):
        self.dialogue_id = 0

    def parse_file(self, filepath):
        dialogues = []

        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            # pattern: speaker "text"
            match = re.match(r'(\w+)\s+"(.+)"', line.strip())

            if match:
                speaker = match.group(1)
                text = match.group(2)

                self.dialogue_id += 1

                dialogue = DialogueEntry(
                    id=self.dialogue_id,
                    speaker=speaker,
                    original_text=text,
                    translated_text="",
                    filename=filepath,
                    line_number=line_number,
                )

                dialogues.append(dialogue)

        return dialogues
