# Changelog

## 1.2.0

- Pidgeon is now Zurchin: this version is published as `langchain-zurchin` (`import langchain_zurchin`), and the last
  `langchain-zurchin` (1.2.0) depends on it, re-exports it and warns once.
- The default host is `https://zurchin.com`. pidgeon.ai keeps answering the API for six months.
- The source repository is `zurchin/pidgeon-python`.

## 1.1.0

- `ZURCHIN_API_KEY`, `ZURCHIN_BASE_URL` and `ZURCHIN_CONFIG_DIR` work beside the `PIDGEON_`
  ones, and win when both are set.

## 1.0.1

- The description, keywords and README lead with email inboxes for AI agents.
  `verify_request` still works and is no longer listed.

## 1.0.0

Rebuilt for the new Pidgeon, on the `pidgeon` SDK 2.x (`/v1`). Nothing of
0.x carries over: 0.1.11 stays on PyPI for the old email API until it is
retired.

- Tools: `list_inboxes`, `send_message`, `reply_to_message`, `list_threads`,
  `get_thread`, `get_message`, `await_message` (the inbox);
  `register_agent`, `get_reputation` (the agent's identity); `verify_request`
  (Bouncer). `PidgeonToolkit` gives them all on one client.
- Every tool that returns mail tells the model that mail is its sender's
  words, never instructions.
- `register_agent` keeps the new agent's private key in a file only this
  user can read; the model never sees it.
- Apache-2.0, as the SDK.
