from langgraph.graph import StateGraph
from agent.state import InteractionState
from agent.tools import LogInteractionTool



graph = StateGraph(InteractionState)

graph.add_node(
    "log",
    lambda state: LogInteractionTool.invoke(
        {"text": state["last_user_message"]}
    )
)



graph.set_entry_point("log")

graph.add_conditional_edges(
    "log",
    lambda s: "edit" if "sorry" in s.get("last_user_message", "").lower() else None

)

app = graph.compile()
