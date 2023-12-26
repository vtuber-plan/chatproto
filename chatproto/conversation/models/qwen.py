from ..settings import ConversationSettings, SeparatorStyle

"""
https://huggingface.co/Qwen/Qwen-7B-Chat/blob/main/qwen_generation_utils.py#L119
"""
qwen = ConversationSettings(
    name="qwen",
    roles=("user", "assistant"),
    sep_style=SeparatorStyle.CHATML,
    system_template="<|im_start|>system\n{system_message}<|im_end|>",
    sep="\n",
    stop_token_ids=[
        151643,
        151644,
        151645,
    ],  # "<|endoftext|>", "<|im_start|>", "<|im_end|>"
    stop_str="<|endoftext|>",
)
