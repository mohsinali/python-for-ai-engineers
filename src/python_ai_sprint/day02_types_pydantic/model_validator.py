from pydantic import BaseModel, model_validator, Field
from typing import Self


class LLMRequest(BaseModel):
    prompt: str
    system_prompt: str | None = None
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1000, gt=0)
    stop_sequences: list[str] = []

    # Runs after all individual fields are validated
    @model_validator(mode="after")
    def check_prompt_not_system_duplicate(self) -> Self:
        if self.system_prompt and self.system_prompt == self.prompt:
            raise ValueError("system_prompt and prompt cannot be identical")
        return self

    # mode="before" runs on raw input dict, before field validation
    @model_validator(mode="before")
    @classmethod
    def normalize_stop_sequences(cls, data: dict) -> dict:
        if "stop_sequences" in data and data["stop_sequences"] is None:
            data["stop_sequences"] = []
        return data


req = LLMRequest(prompt="Explain transformers", temperature=0.5)
print(req.model_dump())  # serialize to dict
