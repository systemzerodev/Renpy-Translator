import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class TranslatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RenPy Translator")

        self.data = []
        self.file_path = None

        # toolbar
        toolbar = tk.Frame(root)
        toolbar.pack(fill="x")

        open_btn = tk.Button(toolbar, text="Open Project", command=self.open_project)
        open_btn.pack(side="left", padx=5, pady=5)

        save_btn = tk.Button(toolbar, text="Save", command=self.save_project)
        save_btn.pack(side="left", padx=5, pady=5)

        # table
        self.tree = ttk.Treeview(
            root, columns=("speaker", "original", "translation"), show="headings"
        )

        self.tree.heading("speaker", text="Speaker")
        self.tree.heading("original", text="Original Text")
        self.tree.heading("translation", text="Translation")

        self.tree.column("speaker", width=80)
        self.tree.column("original", width=300)
        self.tree.column("translation", width=300)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<Double-1>", self.edit_translation)

    def open_project(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if not file_path:
            return

        self.file_path = file_path

        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.refresh_table()

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for entry in self.data:
            self.tree.insert(
                "",
                "end",
                iid=entry["id"],
                values=(
                    entry["speaker"],
                    entry["original_text"],
                    entry["translated_text"],
                ),
            )

    def edit_translation(self, event):
        selected = self.tree.selection()

        if not selected:
            return

        item_id = int(selected[0])

        entry = next(d for d in self.data if d["id"] == item_id)

        new_text = tk.simpledialog.askstring(
            "Edit Translation", "Translation:", initialvalue=entry["translated_text"]
        )

        if new_text is not None:
            entry["translated_text"] = new_text
            self.refresh_table()

    def save_project(self):
        if not self.file_path:
            messagebox.showerror("Error", "No project loaded")
            return

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Saved", "Project saved successfully")


def run():
    root = tk.Tk()
    _ = TranslatorUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()
