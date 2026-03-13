"""
Data models used by the RenPy Translator engine.

These models represent dialogue entries extracted from Ren'Py script files.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DialogueEntry:
    """
    Represents a single dialogue line extracted from a Ren'Py script.
    """

    id: int
    speaker: str
    original_text: str
    translated_text: str
    filename: str
    line_number: int


class DialogueCollection:
    """
    Stores and manages multiple DialogueEntry objects.
    """

    def __init__(self):
        self.dialogues: List[DialogueEntry] = []

    def add(self, dialogue: DialogueEntry):
        """
        Stores and manages multiple DialogueEntry objects.
        """
        self.dialogue.append(dialogue)

    def get_all(self) -> List[DialogueEntry]:
        """
        Return all dialogue entries.
        """
        return self.dialogues

    def get_untranlated(self) -> List[DialogueEntry]:
        """
        Return dialogue entries that have not been translated yet.
        """
        return [d for d in self.dialogues if not d.translated_text]

    def update_translation(self, dialogue_id: int, translation: str):
        """
        Return dialogue entries that have not been translated yet.
        """
        for dialogue in self.dialogues:
            if self.dialogues.id == dialogue_id:
                dialogue.translated_text = translation
                break
