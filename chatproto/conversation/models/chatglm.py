from ..settings import ConversationSettings, SeparatorStyle

# Chatglm default template
chatglm = ConversationSettings(
    name="chatglm",
    roles=("问", "答"),
    system_template="{system_message}\n\n",
    sep_style=SeparatorStyle.CHATGLM,
    sep="\n\n",
    stop_str="\n\n",
)