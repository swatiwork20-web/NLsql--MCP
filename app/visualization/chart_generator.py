# app/visualization/chart_generator.py

from google import genai
from google.oauth2 import service_account
from google.genai.types import GenerateContentConfig
import os
from dotenv import load_dotenv


load_dotenv()

class ChartGenerator:

    def __init__(self):

        # Vertex will use Application Default Credentials
        # self.client = genai.Client()

        # self.model = "gemini-2.5-flash"

        # For local testing with service account key
        # credentials = service_account.Credentials.from_service_account_file(
        #     "bigquery.json"
        # )

        # self.client = genai.Client(credentials=credentials)
        # self.model = "gemini-2.5-flash"
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-2.5-flash"


    async def generate_chart(
        self,
        markdown_data: str,
        chart_type: str,
        metadata: str = ""
    ) -> str:

        system_prompt = """
You are a professional data visualization engineer.

Generate a COMPLETE HTML document using Chart.js CDN.

Rules:
- Output ONLY HTML
- Use Chart.js via CDN
- Responsive
- Use maintainAspectRatio: false
- Fixed height container 500px
- First column = X-axis
- Numeric columns = datasets
- Format large numbers (e.g. 12000 -> 12K)
- Do NOT invent data
- Clean, modern styling
"""

        user_prompt = f"""
Metadata:
{metadata}

Chart Type:
{chart_type}

Markdown Table:
{markdown_data}
"""

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": system_prompt + "\n\n" + user_prompt}
                    ]
                }
            ],
            config=GenerateContentConfig(
                temperature=0.2,
            )
        )

        return response.text