# chatproto
Large Language Model Chat Protocol.

The different chat prompt formats used by different Large Language Models have been a problem for developers. We developed `chatproto` to output the prompt format for different LLMs through a unified interface.

Compared to the `apply_chat_format` function in HuggingFace and the version in FastChat, `ChatProto` can locate the position of each message after applying the template. This makes it very convenient for us to mask out certain conversations during training.

## Quick Start
```python
from chatproto.conversation.history import ConversationHistory
from chatproto.registry import list_conv_settings, get_conv_settings

# Print all available settings
all_settings = list_conv_settings()
print(all_settings)

settings = get_conv_settings("openbuddy")
history = ConversationHistory(
    "SYSTEM_MESSAGE",
    messages=[
        (settings.roles[0], "Hello!"),
        (settings.roles[1], "Hello! How can I assist you today?"),
    ],
    offset=0,
    settings=settings
)
# Apply the template
print(history.get_prompt())

# Get prompt and indices
prompt, indices = history.get_prompt_and_indices()
# Print the start and end offsets of each message in the conversation one by one.
# The start and end offsets here refer to the offsets in the text, not the tokens.
# They do not include any additional characters added in the template.
system_start, system_end = indices[0]
for i, (conv_start, conv_end) in enumerate(indices[1:]):
    print((conv_start, conv_end))
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

