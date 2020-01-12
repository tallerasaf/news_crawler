from pathlib import Path
from typing import List


class FileHandler:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def write_to_file(self, file_name, text):
        file_path = self._get_file_path(file_name)
        with open(file_path, "w") as f:
            f.write(text)

    @staticmethod
    def read_from_file(file_path):
        with open(file_path, "r") as f:
            return f.read()

    def list_files(self) -> List[Path]:
        return [file for file in self.folder_path.iterdir() if file.is_file()]

    def _get_file_path(self, file_name):
        return self.folder_path / f"{file_name}.txt"
