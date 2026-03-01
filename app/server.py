# app/server.py

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

from app.agents.bigquery_agent import BigQueryAgent
from app.agents.visualization_agent import VisualizationAgent
from app.tools.bigquery_tools import BigQueryTools
from app.tools.chart_tools import ChartTools

import os

class AgenticBigQuery:

    def __init__(self):

        project_id = os.getenv("GCP_PROJECT_ID")

        # SQL Tool
        bq_tools = BigQueryTools(project_id)

        # Chart Tool
        chart_tools = ChartTools()

        # Agents
        self.sql_agent = BigQueryAgent(
            tools=[bq_tools.execute_bigquery]
        ).agent

        self.visual_agent = VisualizationAgent(
            tools=[chart_tools.generate_chart]
        ).agent

        self.session_service = InMemorySessionService()

    async def run(self, question, user_id, session_id):

        session = await self.session_service.create_session(
            app_name="BigQueryApp",
            user_id=user_id,
            session_id=session_id,
            state={}
        )

        # --- SQL PHASE ---
        sql_runner = Runner(
            agent=self.sql_agent,
            app_name="BigQueryApp",
            session_service=self.session_service,
        )

        sql_content = types.Content(
            role="user",
            parts=[types.Part(text=question)]
        )

        sql_response = ""

        async for event in sql_runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=sql_content
        ):
            if event.is_final_response():
                sql_response += "".join(
                    p.text for p in event.content.parts if p.text
                )

        # --- VISUALIZATION PHASE ---
        vis_runner = Runner(
            agent=self.visual_agent,
            app_name="BigQueryApp",
            session_service=self.session_service,
        )

        vis_content = types.Content(
            role="user",
            parts=[types.Part(text=sql_response)]
        )

        vis_response = ""

        async for event in vis_runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=vis_content
        ):
            if event.is_final_response():
                vis_response += "".join(
                    p.text for p in event.content.parts if p.text
                )

        return vis_response