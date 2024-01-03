
from ..settings import ConversationSettings, SeparatorStyle

# cutegpt default template
cutegpt = ConversationSettings(
    name="cutegpt",
    roles=("问：", "答：\n"),
    sep_style=SeparatorStyle.NO_COLON_TWO,
    sep="\n",
    sep2="\n",
    stop_str="<end>",
)
