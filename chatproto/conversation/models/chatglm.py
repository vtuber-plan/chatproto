from ..settings import ConversationSettings, SeparatorStyle

# Chatglm default template
chatglm = ConversationSettings(
    name="chatglm",
    roles=("问", "答"),
    system_template="{system_message}\n\n",
    sep_style=SeparatorStyle.CHATGLM,
    sep="\n",
)

chatglm2 = ConversationSettings(
    name="chatglm2",
    roles=("问", "答"),
    system_template="{system_message}\n\n",
    sep_style=SeparatorStyle.CHATGLM,
    sep="\n\n",
    stop_str="\n\n",
)

chatglm3 = ConversationSettings(
    name="chatglm3",
    system_template="<|system|>\n {system_message}",
    roles=("<|user|>", "<|assistant|>"),
    sep_style=SeparatorStyle.CHATGLM3,
    sep = "\n",
    stop_token_ids=[
        64795,
        64797,
        2,
    ],  # "<|user|>", "<|observation|>", "</s>"
)