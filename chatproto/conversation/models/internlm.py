from ..settings import ConversationSettings, SeparatorStyle

# internlm default template
# FIXME: round_sep="<s>",
internlm = ConversationSettings(
    name="internlm",
    roles=("<|User|>", "<|Bot|>"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep="<eoh>\n",
    sep2="<eoa>\n",
    stop_str="<eoa>",
    stop_token_ids=[1, 2]
)
