from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal


# # --- Basic model ---
class LLMConfig(BaseModel):
    model: str
    temperature: float = 0.7
    max_tokens: int = 1000
    streaming: bool = False


# # Pydantic parses and validates on instantiation
config = LLMConfig(model="gpt-4o", temperature=0.9)
print(config.model)  # gpt-4o
print(config.max_tokens)  # 1000 (default)

# # Type coercion — Pydantic tries to convert compatible types
config2 = LLMConfig(model="gpt-4o", temperature="0.5")  # string → float ✅
print(config2.temperature)  # 0.5

# # Validation error — clear, immediate, structured
try:
    bad = LLMConfig(model="gpt-4o", temperature="hot")  # can't convert
except Exception as e:
    print(e)
# # Output: temperature: Input should be a valid number ...


# # --- Field() — add constraints and metadata ---
class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(..., min_length=1, max_length=10000)
    # ... means required — no default


msg = Message(role="user", content="Hello!")
print(msg)  # role='user' content='Hello!'


# --- field_validator — custom validation logic ---
class PromptTemplate(BaseModel):
    template: str
    input_variables: list[str]

    @field_validator("template")
    @classmethod
    def template_must_have_variables(cls, v: str) -> str:
        if "{" not in v:
            raise ValueError("Template must contain at least one {variable}")
        return v.strip()  # you can also transform the value here

    @field_validator("input_variables")
    @classmethod
    def variables_must_be_unique(cls, v: list[str]) -> list[str]:
        if len(v) != len(set(v)):
            raise ValueError("Duplicate variable names not allowed")
        return v


# Valid
pt = PromptTemplate(
    template="Answer this question: {question}", input_variables=["question"]
)

# Raises immediately
try:
    PromptTemplate(template="No variables here", input_variables=["x"])
except Exception as e:
    print(e)
