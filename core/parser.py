"""
RenPy script parser

Responsible for scanning .rpy files and extracting dialogue text.
"""

import os
import re


def find_rpy_files(game_folder: str):
    """Find all .rpy files in the Ren'Py game directory."""
    rpy_files = []

    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(".rpy"):
                rpy_files.append(os.path.join(root, file))

    return rpy_files


def extract_dialogue(line: str):
    """Extract dialogue text inside quotes."""
    match = re.search(r'"(.*?)"', line)
    if match:
        return match.group(1)
    return None
