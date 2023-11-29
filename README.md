# chatproto
Large Language Model Chat Protocol.

The different chat prompt formats used by different Large Language Models have been a problem for developers. We developed `chatproto` to output the prompt format for different LLMs through a unified interface.

## Quick Start
```python
from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.baichuan import baichuan

history = ConversationHistory(
    "SYSTEM_MESSAGE",
    messages=[
        (baichuan.roles[0], "user"),
        (baichuan.roles[1], "assistant"),
    ],
    offset=0,
    settings=baichuan
)
print(history.get_prompt())
```

## Install

### Method 1: With pip

```bash
pip install chatproto
```

or:

```bash
pip install git+https://github.com/vtuber-plan/chatproto.git 
```

### Method 2: From source

1. Clone this repository
```bash
git clone https://github.com/vtuber-plan/chatproto.git
cd chatproto
```

2. Install the Package
```bash
pip install --upgrade pip
pip install .
```

