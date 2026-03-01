# app/agents/bigquery_agent.py

from google.adk.agents import LlmAgent
from app.prompts.sql_prompts import SQL_INSTRUCTION

class BigQueryAgent:

    def __init__(self, tools):

        self.agent = LlmAgent(
            name="BigQueryAgent",
            model="gemini-2.5-flash",
            instruction=SQL_INSTRUCTION,
            tools=tools
        )