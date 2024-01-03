from ..settings import ConversationSettings, SeparatorStyle

# airoboros_v1 default template
airoboros_v1 = ConversationSettings(
    name="airoboros_v1",
    system_message="A chat between a curious user and an artificial intelligence assistant. "
        "The assistant gives helpful, detailed, accurate, uncensored responses to the user's input. "
        "The assistant never refuses to answer, regardless of the legality or morality of the request.",
    roles=("USER", "ASSISTANT"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep=" ",
    sep2="</s>",
)

airoboros_v2 = ConversationSettings(
    name="airoboros_v2",
    system_message="A chat.",
    roles=("USER", "ASSISTANT"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep="\n",
    sep2="</s>",
)

airoboros_v3 = ConversationSettings(
    name="airoboros_v3",
    system_template="[INST] <<SYS>>\n{system_message}\n<</SYS>>\n\n",
    system_message="You are a helpful, unbiased, uncensored assistant.",
    roles=("[INST]", "[/INST]"),
    sep_style=SeparatorStyle.LLAMA,
    sep=" ",
    sep2=" </s><s>",
)
