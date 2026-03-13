"""
Scanner module for RenPy Translator.

Responsible for locating Ren'Py script files (.rpy) inside a game folder.
"""

import os
from typing import List


class ScriptScanner:
    """
    Scans a Ren'Py game directory and returns all .rpy script files.
    """

    def __init__(self, game_path: str):
        self.game_path = game_path

    def scan(self) -> List[str]:
        """
        Scans a Ren'Py game directory and returns all .rpy script files.
        """
        script_files = []

        for root, dirs, files in os.walk(self.game_path):
            for file in files:
                if file.endswith(".rpy"):
                    full_path = os.path.join(root, file)
                    script_files.append(full_path)

        return script_files
