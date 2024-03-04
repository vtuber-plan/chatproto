from ..settings import ConversationSettings, SeparatorStyle

# Yi template: https://huggingface.co/01-ai/Yi-6B-Chat/blob/main/tokenizer_config.json
yi = ConversationSettings(
    name="yi",
    roles=("<|im_start|>user", "<|im_start|>assistant"),
    sep_style=SeparatorStyle.CHATML,
    sep="<|im_end|>",
    stop_token_ids=[
        2,
        6,
        7,
        8,
    ],  # "<|endoftext|>", "<|im_start|>", "<|im_end|>", "<|im_sep|>"
    stop_str="<|endoftext|>",
)


Yi = yi.alias("Yi")