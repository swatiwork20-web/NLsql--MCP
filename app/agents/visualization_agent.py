from google.adk.agents import LlmAgent
from app.prompts.chart_prompts import CHART_INSTRUCTION

class VisualizationAgent:

    def __init__(self, tools):

        self.agent = LlmAgent(
            name="VisualizationAgent",
            model="gemini-2.5-flash",
            instruction=CHART_INSTRUCTION,
            tools=tools
        )