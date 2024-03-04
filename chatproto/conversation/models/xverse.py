from ..settings import ConversationSettings, SeparatorStyle

# xverse template: https://huggingface.co/xverse/XVERSE-13B-Chat/blob/main/modeling_xverse.py#L780
xverse = ConversationSettings(
    name="xverse",
    system_template="Human: {system_message}\n",
    roles=("Human", "Assistant"),
    sep_style=SeparatorStyle.ADD_COLON_TWO,
    sep="\n\n",
    sep2="<|endoftext|>",
    stop_token_ids=[
        3,
    ],  # eos_token_id: <|endoftext|>
    stop_str="<|endoftext|>",
)


XVERSE = xverse.alias("XVERSE")