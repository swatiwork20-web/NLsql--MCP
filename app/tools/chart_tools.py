# app/tools/chart_tools.py

from google.adk.tools import ToolContext
from app.visualization.chart_generator import ChartGenerator


class ChartTools:

    def __init__(self):
        self.chart_gen = ChartGenerator()

    async def generate_chart(
        self,
        markdown_data: str,
        chart_type: str,
        metadata: str,
        tool_context: ToolContext
    ) -> str:

        return await self.chart_gen.generate_chart(
            markdown_data,
            chart_type,
            metadata
        )