from ..settings import ConversationSettings, SeparatorStyle

# AquilaChat default template
# source: https://github.com/FlagAI-Open/FlagAI/blob/master/examples/Aquila/Aquila-chat/cyg_conversation.py
aquila_chat = ConversationSettings(
    name="aquila-chat",
    system_message="A chat between a curious human and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the human's questions.",
    roles=("Human", "Assistant"),
    sep_style=SeparatorStyle.ADD_COLON_SINGLE,
    sep="###",
    sep2="",
    stop_str=["###", "</s>", "[UNK]"],
)

# AquilaChat2-34B default template
# source: https://huggingface.co/BAAI/AquilaChat2-34B/blob/4608b75855334b93329a771aee03869dbf7d88cc/predict.py#L212
aquila_legacy = ConversationSettings(
    name="aquila-legacy",
    system_message="A chat between a curious human and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the human's questions.\n\n",
    roles=("### Human: ", "### Assistant: "),
    sep_style=SeparatorStyle.NO_COLON_TWO,
    sep="\n",
    sep2="</s>",
    stop_str=["</s>", "[UNK]"],
)

# AquilaChat2-7B-16K and AquilaChat2-34B-16K default template
# source: https://huggingface.co/BAAI/AquilaChat2-34B/blob/4608b75855334b93329a771aee03869dbf7d88cc/predict.py#L227
aquila = ConversationSettings(
    name="aquila",
    system_message="A chat between a curious human and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the human's questions.",
    roles=("Human", "Assistant"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep="###",
    sep2="</s>",
    stop_str=["</s>", "[UNK]"],
)


# AquilaChat2-7B default template
# source: https://huggingface.co/BAAI/AquilaChat2-34B/blob/4608b75855334b93329a771aee03869dbf7d88cc/predict.py#L242
aquila_v1 = ConversationSettings(
    name="aquila-v1",
    roles=("<|startofpiece|>", "<|endofpiece|>"),
    sep_style=SeparatorStyle.NO_COLON_TWO,
    sep="",
    sep2="</s>",
    stop_str=["</s>", "<|endoftext|>"],
)
