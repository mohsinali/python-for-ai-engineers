from pydantic import BaseModel
import json


class ChatHistory(BaseModel):
    session_id: str
    messages: list[dict]
    total_tokens: int = 0


history = ChatHistory(
    session_id="abc123",
    messages=[{"role": "user", "content": "Hello"}],
    total_tokens=42,
)


# # --- To dict ---
d = history.model_dump()
print(type(d))  # <class 'dict'>

# # --- To JSON string ---
j = history.model_dump_json()
# print(j)  # {"session_id":"abc-123","messages":[...],"total_tokens":42}

# # --- From dict ---
data = {"session_id": "xyz", "messages": "", "total_tokens": "10"}
h2 = ChatHistory.model_validate(data)

# # --- From JSON string ---
json_str = '{"session_id":"xyz","messages":[],"total_tokens":10}'
h3 = ChatHistory.model_validate_json(json_str)

# # --- Exclude fields, include only certain fields ---
print(history.model_dump(exclude={"total_tokens"}))
print(history.model_dump(include={"session_id", "messages"}))
