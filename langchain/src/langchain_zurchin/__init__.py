"""Pidgeon for LangChain agents: an email inbox of its own, and a key for Sign in with Pidgeon."""

from langchain_zurchin._version import __version__
from langchain_zurchin.toolkit import PidgeonToolkit
from langchain_zurchin.tools import (
    AwaitMessage,
    GetMessage,
    GetReputation,
    GetThread,
    ListInboxes,
    ListThreads,
    PidgeonTool,
    RegisterAgent,
    ReplyToMessage,
    SendMessage,
    VerifyRequest,
    client_from_env,
)

__all__ = [
    "AwaitMessage",
    "GetMessage",
    "GetReputation",
    "GetThread",
    "ListInboxes",
    "ListThreads",
    "PidgeonTool",
    "PidgeonToolkit",
    "RegisterAgent",
    "ReplyToMessage",
    "SendMessage",
    "VerifyRequest",
    "__version__",
    "client_from_env",
]
