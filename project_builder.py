from pathlib import Path


class ProjectBuilder:

    def create_project(
        self,
        project_data,
        base_folder="generated"
    ):

        project_name = project_data.get(
            "project_name",
            "GeneratedProject"
        )

        safe_name = "".join(
            c for c in project_name
            if c.isalnum() or c in "_- "
        ).strip()

        root = Path(base_folder) / safe_name

        root.mkdir(
            parents=True,
            exist_ok=True
        )

        files = project_data.get(
            "files",
            []
        )

        for file_data in files:

            path = root / file_data["path"]

            path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            path.write_text(
                file_data["content"],
                encoding="utf-8"
            )

        return str(root)
