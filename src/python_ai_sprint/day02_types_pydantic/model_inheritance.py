from pydantic import BaseModel, Field
from typing import Literal


# --- Base schema ---
class BaseMessage(BaseModel):
    content: str
    role: str


# --- Specialized versions ---
class SystemMessage(BaseMessage):
    role: Literal["system"] = "system"


class HumanMessage(BaseMessage):
    role: Literal["user"] = "user"


class AIMessage(BaseMessage):
    role: Literal["assistant"] = "assistant"
    finish_reason: Literal["stop", "length", "tool_calls"] | None = None
    usage_tokens: int = 0


# Child classes inherit all parent validation
ai_msg = AIMessage(content="LangChain is a framework...", finish_reason="stop")
print(ai_msg.model_dump())

# --- This is exactly how LangChain structures its messages internally ---
# Once you know this, reading LangChain source is trivial
