from pathlib import Path

import gradio as gr

from generator import GeminiGenerator
from project_builder import ProjectBuilder
from zip_exporter import ZipExporter


generator = GeminiGenerator()
builder = ProjectBuilder()
zipper = ZipExporter()


def build_project(prompt):

    try:

        data = generator.generate_project(
            prompt
        )

        folder = builder.create_project(
            data
        )

        zip_file = zipper.export(
            folder
        )

        preview_lines = []

        for file in data["files"]:

            preview_lines.append(
                f"📄 {file['path']}"
            )

        preview_text = "\n".join(
            preview_lines
        )

        return (
            data["project_name"],
            preview_text,
            zip_file
        )

    except Exception as e:

        return (
            "ERROR",
            str(e),
            None
        )


def random_ideas():

    try:
        return generator.generate_random_ideas()

    except Exception as e:
        return str(e)


def category_ideas(category):

    try:
        return generator.generate_category_ideas(
            category
        )

    except Exception as e:
        return str(e)


def launch_ui():

    with gr.Blocks(
        title="AI Project Builder"
    ) as app:

        gr.Markdown(
            """
# 🚀 AI Project Builder

Generate complete Python 3.14 projects using Gemini.
"""
        )

        with gr.Tab("Project Builder"):

            prompt = gr.Textbox(
                label="Project Description",
                lines=10,
                placeholder="""
Create a FastAPI Todo App with:

- SQLite
- CRUD
- Authentication
- requirements.txt
- README.md
"""
            )

            generate_btn = gr.Button(
                "Generate Project"
            )

            project_name = gr.Textbox(
                label="Project Name"
            )

            preview = gr.Textbox(
                label="Generated Files",
                lines=20
            )

            zip_file = gr.File(
                label="Download ZIP"
            )

            generate_btn.click(
                fn=build_project,
                inputs=prompt,
                outputs=[
                    project_name,
                    preview,
                    zip_file
                ]
            )

        with gr.Tab("Idea Generator"):

            gr.Markdown(
                "Generate unique software project ideas."
            )

            random_btn = gr.Button(
                "🎲 Random Ideas"
            )

            ideas_output = gr.Textbox(
                label="Ideas",
                lines=25
            )

            random_btn.click(
                fn=random_ideas,
                outputs=ideas_output
            )

        with gr.Tab("Category Ideas"):

            category = gr.Dropdown(
                [
                    "AI",
                    "Machine Learning",
                    "Automation",
                    "Web Development",
                    "Cybersecurity",
                    "Data Science",
                    "Game Development",
                    "Developer Tools",
                    "Startup Ideas"
                ],
                value="AI",
                label="Category"
            )

            category_btn = gr.Button(
                "Generate Ideas"
            )

            category_output = gr.Textbox(
                label="Results",
                lines=25
            )

            category_btn.click(
                fn=category_ideas,
                inputs=category,
                outputs=category_output
            )

    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )
