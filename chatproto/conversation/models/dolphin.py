
from ..settings import ConversationSettings, SeparatorStyle

# ehartford/dolphin-2.2.1-mistral-7b template
# reference: https://huggingface.co/ehartford/dolphin-2.2.1-mistral-7b#training

dolphin = ConversationSettings(
    name="dolphin",
    system_template="<|im_start|>system\n{system_message}",
    system_message="You are Dolphin, a helpful AI assistant.",
    roles=("<|im_start|>user", "<|im_start|>assistant"),
    sep_style=SeparatorStyle.CHATML,
    sep="<|im_end|>",
    stop_token_ids=[32000, 32001],
)
