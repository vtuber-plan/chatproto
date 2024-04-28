from ..settings import ConversationSettings, SeparatorStyle

# Phi default template
phi = ConversationSettings(
    name="phi",
    roles=("<|user|>", "<|assistant|>"),
    sep_style=SeparatorStyle.ADD_NEW_LINE_SINGLE,
    system_template="<|system|>\n{system_message}",
    sep="<|end|>\n",
    stop_str="<|end|>",
)
