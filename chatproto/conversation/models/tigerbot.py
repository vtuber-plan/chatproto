from ..settings import ConversationSettings, SeparatorStyle

# tigerbot default template
tigerbot = ConversationSettings(
    name="tigerbot",
    system_message="A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions.",
    roles=("### Instruction", "### Response"),
    sep_style=SeparatorStyle.ROBIN,
    sep="\n\n",
    stop_str="###",
)
