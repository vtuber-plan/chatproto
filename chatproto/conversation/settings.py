import dataclasses
from enum import auto, Enum
from typing import List, Any, Optional, Tuple


class SeparatorStyle(Enum):
    """Separator styles."""

    ADD_COLON_SINGLE = auto()
    ADD_COLON_TWO = auto()
    ADD_COLON_SPACE_SINGLE = auto()
    NO_COLON_SINGLE = auto()
    NO_COLON_TWO = auto()
    ADD_NEW_LINE_SINGLE = auto()
    DOLLY = auto()
    RWKV = auto()
    PHOENIX = auto()
    LLAMA = auto()
    CHATGLM = auto()
    CHATGLM3 = auto()
    CHATML = auto()
    ROBIN = auto()


@dataclasses.dataclass
class ConversationSettings:
    # The name of this settings
    name: str
    # Two roles
    roles: List[str]
    # Separators
    sep_style: SeparatorStyle
    sep: str
    sep2: Optional[str] = None
    # Default system message
    system_message: Optional[str] = None
    # The template of the system prompt
    system_template: str = "{system_message}"
    # Stop criteria (the default one is EOS token)
    stop_str: str = None
    # Stops generation if meeting any token in this list
    stop_token_ids: List[int] = None

    def copy(self):
        return ConversationSettings(
            name=self.name,
            roles=self.roles,
            system_template=self.system_template,
            sep_style=self.sep_style,
            sep=self.sep,
            sep2=self.sep2,
            stop_str=self.stop_str,
            stop_token_ids=self.stop_token_ids,
        )
    
    def alias(self, new_name: str):
        return ConversationSettings(
            name=new_name,
            roles=self.roles,
            system_template=self.system_template,
            sep_style=self.sep_style,
            sep=self.sep,
            sep2=self.sep2,
            stop_str=self.stop_str,
            stop_token_ids=self.stop_token_ids,
        )

