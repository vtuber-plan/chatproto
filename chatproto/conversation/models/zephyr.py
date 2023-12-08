from ..settings import ConversationSettings, SeparatorStyle

# zephyr template
zephyr = ConversationSettings(
    name="zephyr",
    roles=("<|user|>", "<|assistant|>"),
    system_template="<|system|>\n{system_message}",
    sep_style=SeparatorStyle.ADD_NEW_LINE_SINGLE,
    sep="</s>\n",
)