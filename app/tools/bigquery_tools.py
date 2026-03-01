# app/tools/bigquery_tools.py

from google.cloud import bigquery
from google.oauth2 import service_account
from google.adk.tools import ToolContext

import os

class BigQueryTools:

    def __init__(self, project_id: str):
        #self.client = bigquery.Client(project=project_id)
        #   credentials = service_account.Credentials.from_service_account_file(
        #     "bigquery.json" 
        # )
        #   self.client = bigquery.Client(
        #     credentials=credentials,
        #     project=project_id
        #   )

        pass
    def execute_bigquery(
        self,
        queries: list[str],
        tool_context: ToolContext
    ) -> str:
        
        #mock result for test
        return str([{
            "year": 2023,
            "sales": 100000
        }, {
            "year": 2024,
            "sales": 120000
        }])

        result_blocks = []

        for query in queries:

            job = self.client.query(query)
            result = job.result()

            rows = [dict(row) for row in result]

            result_blocks.append({
                "query": query,
                "rows": rows
            })

        return str(result_blocks)