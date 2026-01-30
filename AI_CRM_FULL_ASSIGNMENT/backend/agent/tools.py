from langchain_core.tools import StructuredTool
from pydantic import BaseModel
from typing import Dict
import json


class LogInteractionInput(BaseModel):
    text: str


def log_interaction(text: str) -> Dict:
    # for now, return dummy structured output
    # (LLM logic can stay as-is later)
    return {
        "hcp_name": "Dr Smith",
        "topics": "Product X efficiency",
        "sentiment": "Positive"
    }


LogInteractionTool = StructuredTool.from_function(
    name="log_interaction",
    description="Extract HCP interaction details from user text",
    func=log_interaction,
    args_schema=LogInteractionInput,
)
