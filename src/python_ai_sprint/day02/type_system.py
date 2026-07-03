from typing import Union, Literal, Optional, Any
from collections.abc import Sequence, Callable
from typing import TypeVar
from typing import TypedDict


def get_embeddings(texts: list[str]) -> list[list[float]]:
    return [[2.5], [0.88]]
    print("get_embeddings")


def process_input(data: str | list[str]) -> str:
    if isinstance(data, list):
        return " ".join(data)
    return data


# ## Print
# print(process_input(["Mohsin", "Ali"]))


Role = Literal["system", "user", "assistant"]


def create_message(role: Role, content: str) -> dict:
    return {"role": role, "content": content}


# ## Print
# print(create_message("user", "Hello"))


def get_system_prompt(template: str | None = None) -> str:
    return template or "You are a helpful assistant."


# # --- TypeVar — for generic functions that preserve type ---
# from typing import TypeVar
T = TypeVar("T")


def first(items: list[T]) -> T | None:
    return items[0] if items else None


class Message(TypedDict):
    role: Role
    content: str


messages: list[Message] = [{"role": "user", "content": "What is LangChain?"}]
