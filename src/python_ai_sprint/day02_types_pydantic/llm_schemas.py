from pydantic import BaseModel, Field, field_validator
from typing import Literal, Any
from datetime import datetime


class LLMInput(BaseModel):
    """Schema for everything going INTO an LLM call."""

    messages: list[dict]
    model: Literal["gpt-4o", "gpt-4o-mini", "claude-sonnet-4-6"] = "gpt-4o-mini"
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, gt=0, le=128000)
    stream: bool = False
    metadata: dict[str, Any] = {}

    @field_validator("messages")
    @classmethod
    def messages_not_empty(cls, v: list) -> list:
        if not v:
            raise ValueError("Messages list cannot be empty.")

        for msg in v:
            if "role" not in msg or "content" not in msg:
                raise ValueError("Each message must have 'role' and 'content'.")

        return v


class TokenUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class LLMOutput(BaseModel):
    """Schema for everything coming OUT of an LLM call."""

    content: str
    model: str
    finish_reason: Literal["stop", "length", "tool_calls", "error"]
    usage: TokenUsage
    latency_ms: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    @property
    def cost_estimate_usd(self) -> float:
        # rough GPT-4o-mini pricing
        return (self.usage.total_tokens / 1_000_000) * 0.60


# Usage
user_input = LLMInput(
    messages=[{"role": "user", "content": "What is an AI agent?"}], temperature=0.5
)

# This is what you'd build from the API response
response = LLMOutput(
    content="An AI agent is a system that...",
    model="gpt-4o-mini",
    finish_reason="stop",
    usage=TokenUsage(prompt_tokens=20, completion_tokens=80, total_tokens=100),
    latency_ms=342.5,
)

print(f"Cost: ${response.cost_estimate_usd:.6f}")
print(response.model_dump_json(indent=2))
