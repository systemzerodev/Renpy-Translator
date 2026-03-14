"""
Exporter module

Responsible for saving extracted dialogue into a translation project file.
"""

import json


class DialogueExporter:
    def export_to_json(self, dialogues, output_file):
        data = []

        for d in dialogues:
            data.append(
                {
                    "id": d.id,
                    "speaker": d.speaker,
                    "original_text": d.original_text,
                    "translated_text": d.translated_text,
                    "filename": d.filename,
                    "line_number": d.line_number,
                }
            )

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\nExported {len(data)} dialogues to {output_file}")
