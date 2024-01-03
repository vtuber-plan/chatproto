from ..settings import ConversationSettings, SeparatorStyle

"""
https://huggingface.co/baichuan-inc/Baichuan-13B-Chat/blob/main/modeling_baichuan.py#L555
"""
# Baichuan default template
baichuan = ConversationSettings(
    name="baichuan",
    roles=("<reserved_102>", "<reserved_103>"),
    sep_style=SeparatorStyle.NO_COLON_SINGLE,
    sep="",
    stop_token_ids=[2, 195],
)


"""
https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat/blob/main/modeling_baichuan.py#L555
"""
# Baichuan default template
baichuan2 = ConversationSettings(
    name="baichuan2",
    roles=("<reserved_106>", "<reserved_107>"),
    sep_style=SeparatorStyle.NO_COLON_SINGLE,
    sep="",
    stop_token_ids=[2, 195],
)
