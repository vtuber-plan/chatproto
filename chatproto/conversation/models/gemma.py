from ..settings import ConversationSettings, SeparatorStyle

# Gemma
# reference: https://huggingface.co/google/gemma-7b-it?text=%3Cstart_of_turn%3Euser%0AHow+does+the+brain+work%3F%3Cend_of_turn%3E%0A%3Cstart_of_turn%3Emodel
gemma = ConversationSettings(
    name="gemma",
    roles=("<start_of_turn>user", "<start_of_turn>model"),
    system_template="<bos>{system_message}",
    sep_style=SeparatorStyle.ADD_NEW_LINE_SINGLE,
    sep="<end_of_turn>\n",
    stop_str="<end_of_turn>",
)

# FIXME: <bos>
