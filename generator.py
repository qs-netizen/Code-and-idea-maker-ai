import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiGenerator:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_project(self, prompt: str):

        system_prompt = f"""
You are an expert Python software architect.

IMPORTANT RULES:

1. Generate code for Python 3.14.
2. Use modern syntax.
3. Use compatible libraries.
4. Create complete projects.
5. Include requirements.txt.
6. Include README.md.
7. Include install.bat.
8. Include run.bat.
9. Return ONLY JSON.

JSON FORMAT:

{{
  "project_name":"ProjectName",
  "files":[
    {{
      "path":"main.py",
      "content":"print('hello')"
    }}
  ]
}}

PROJECT REQUEST:

{prompt}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=system_prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text[7:]

        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text)

    def generate_random_ideas(self):

        prompt = """
Generate 20 UNIQUE software project ideas.

Requirements:

- Python 3.14
- Modern
- Useful

For each idea provide:

Name
Description
Tech Stack
Difficulty
Estimated Build Time
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    def generate_category_ideas(
        self,
        category
    ):

        prompt = f"""
Generate 10 software project ideas.

Category:
{category}

Requirements:

- Python 3.14
- Modern
- Useful
- Portfolio worthy

Return:

Name
Description
Tech Stack
Difficulty
Estimated Time
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
