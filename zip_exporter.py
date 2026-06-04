import shutil
from pathlib import Path


class ZipExporter:

    def export(self, folder_path):

        folder = Path(folder_path)

        archive_path = shutil.make_archive(
            str(folder),
            "zip",
            folder
        )

        return archive_path
