from ..settings import ConversationSettings, SeparatorStyle

# xgen template: https://huggingface.co/Salesforce/xgen-7b-8k-inst
xgen = ConversationSettings(
    name="xgen",
    system_message="A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n\n",
    roles=("### Human", "### Assistant"),
    sep_style=SeparatorStyle.ADD_COLON_SINGLE,
    sep="\n",
    stop_token_ids=[50256],
)
