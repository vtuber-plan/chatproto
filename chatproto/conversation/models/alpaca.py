from ..settings import ConversationSettings, SeparatorStyle

# Alpaca default template
baichuan = ConversationSettings(
    name="alpaca",
    system_message="Below is an instruction that describes a task. Write a response that appropriately completes the request.",
    roles=("### Instruction", "### Response"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep="\n\n",
    sep2="</s>",
)
