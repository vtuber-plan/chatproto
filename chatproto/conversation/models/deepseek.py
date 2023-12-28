from ..settings import ConversationSettings, SeparatorStyle

# Deepseek default template
deepseek = ConversationSettings(
    name="deepseek",
    roles=("User", "Assistant"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    system_template="{system_message}\n",
    sep="\n\n",
    sep2="<｜end▁of▁sentence｜>",
    stop_str="<｜end▁of▁sentence｜>",
)

