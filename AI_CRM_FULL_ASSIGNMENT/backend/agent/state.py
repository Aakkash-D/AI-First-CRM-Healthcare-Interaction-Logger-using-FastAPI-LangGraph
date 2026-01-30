from typing import TypedDict, List


class InteractionState(TypedDict, total=False):
    # raw user input
    last_user_message: str

    # extracted fields
    hcp_name: str
    date: str
    time: str
    topics: str
    sentiment: str
    materials: List[str]
    outcomes: str
    follow_up: str
