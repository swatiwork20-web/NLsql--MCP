# app/tools/analytics_tools.py

from google.adk.tools import ToolContext

def detect_growth(
    results: list,
    tool_context: ToolContext
) -> dict:

    if len(results) < 2:
        return {"growth": None}

    prev = results[-2]
    curr = results[-1]

    return {"growth": curr - prev}