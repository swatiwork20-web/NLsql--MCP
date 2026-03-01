from fastmcp import FastMCP
from app.server import AgenticBigQuery
import uuid

mcp = FastMCP("BigQueryAnalytics")

engine = AgenticBigQuery()

@mcp.tool()
async def analytics_agent(question: str):

    return await engine.run(
        question=question,
        user_id="default_user",
        session_id=str(uuid.uuid4())
    )

if __name__ == "__main__":
    #mcp.run()
    mcp.run(transport="http", host="127.0.0.1", port=8001)