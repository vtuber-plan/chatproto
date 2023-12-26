from ..settings import ConversationSettings, SeparatorStyle

# Llama default template
llama = ConversationSettings(
    name="llama",
    system_template="[INST] <<SYS>>\n{system_message}\n<</SYS>>\n\n",
    roles=("[INST]", "[/INST]"),
    sep_style=SeparatorStyle.LLAMA,
    sep=" ",
    sep2=" </s><s>",
    stop_str=["[/INST]", "[INST]"]
)

llama1 = llama.alias("llama1")
llama2 = llama.alias("llama2")