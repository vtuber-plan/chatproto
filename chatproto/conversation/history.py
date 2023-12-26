
from typing import List, Optional, Tuple
import dataclasses

from .settings import ConversationSettings, SeparatorStyle

def create_system_prompt(settings: ConversationSettings, system: Optional[str]) -> str:
    if system is None:
        system_prompt = ""
    else:
        system_prompt = settings.system_template.format(system_message=system)
    return system_prompt

def create_add_colon_single(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt + settings.sep
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + ": " + message + settings.sep
            prefix = ret + role + ": "
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + ":"
        ret += section
    return ret, indices

def create_add_colon_two(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    seps = [settings.sep, settings.sep2]
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt + seps[0]
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + ": " + message + seps[i % 2]
            prefix = ret + ": "
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + ":"
        ret += section
    return ret, indices

def create_no_colon_single(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt + settings.sep
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + message + settings.sep
            prefix = ret + role
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role
        ret += section
    return ret, indices

def create_no_colon_two(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    seps = [settings.sep, settings.sep2]
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt + seps[0]
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + message + seps[i % 2]
            prefix = ret + role
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role
        ret += section
    return ret, indices

def create_add_new_line_single(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt + settings.sep
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + "\n" + message + settings.sep
            prefix = ret + role + "\n"
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + "\n"
        ret += section
    return ret, indices

def create_dolly(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    seps = [settings.sep, settings.sep2]
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + ":\n" + message + seps[i % 2]
            if i % 2 == 1:
                section += "\n\n"
            prefix = ret + role + ":\n"
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + ":\n"
        ret += section
    return ret, indices

def create_rwkv(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            msg_clean = message.replace("\r\n", "\n").replace("\n\n", "\n")
            section = role + ": " + msg_clean
            prefix = ret + role + ": "
            indices.append((len(prefix), len(prefix) + len(msg_clean)))
        else:
            section = role + ":"
        ret += section
    return ret, indices

def create_phoenix(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            section = role + ": " + "<s>" + message + "</s>"
            prefix = ret + role + ": " + "<s>"
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + ": " + "<s>"
        ret += section
    return ret, indices

def create_chatglm(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            section = ""
            prefix = ""
            if i % 2 == 0:
                section += f"[Round {i+1}]\n\n"
                prefix += ret + f"[Round {i+1}]\n\n"
            section += role + "：" + message + settings.sep
            prefix += role + "："
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = role + "："
        ret += section
    return ret, indices

def create_llama(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    seps = [settings.sep, settings.sep2]
    indices = []
    system_prompt = create_system_prompt(settings, system)
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            if i == 0:
                section = message + " "
                prefix = ret
            else:
                section = settings.roles[i % 2] + " " + message + seps[i % 2]
                prefix = ret + settings.roles[i % 2] + " "
            if i == len(messages) - 1:
                section += settings.roles[(i + 1) % 2]
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = settings.roles[i % 2]
        ret += section
    return ret, indices

def create_chatml(settings: ConversationSettings, system: Optional[str], messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
    im_start, im_end = "<|im_start|>", "<|im_end|>"
    indices = []
    system_prompt = create_system_prompt(settings, system)
    if len(system_prompt) != 0:
        system_prompt += settings.sep
    indices.append((0, len(system_prompt)))

    ret = system_prompt
    for i, (role, message) in enumerate(messages):
        if message:
            section = im_start + role + "\n" + message + im_end + settings.sep
            prefix = ret + im_start + role + "\n"
            indices.append((len(prefix), len(prefix) + len(message)))
        else:
            section = im_start + role + "\n"
        ret += section
    return ret, indices

@dataclasses.dataclass
class ConversationHistory:
    """A class that keeps all conversation history."""

    # System prompts
    system: Optional[str]
    # All messages
    messages: List[Tuple[str, str]]
    # Offset of few shot examples
    offset: int

    settings: ConversationSettings

    def get_prompt_and_indices(self) -> Tuple[str, List[Tuple[int, int]]]:
        if self.system is None:
            system_prompt = ""
        else:
            system_prompt = self.settings.system_template.format(system_message=self.system)
        if self.settings.sep_style == SeparatorStyle.ADD_COLON_SINGLE:
            ret, indices = create_add_colon_single(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.ADD_COLON_TWO:
            ret, indices = create_add_colon_two(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.NO_COLON_SINGLE:
            ret, indices = create_no_colon_single(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.NO_COLON_TWO:
            ret, indices = create_no_colon_two(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.ADD_NEW_LINE_SINGLE:
            ret, indices = create_add_new_line_single(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.DOLLY:
            ret, indices = create_dolly(self.settings, self.system, self.messages)
            return ret, indices
        elif self.settings.sep_style == SeparatorStyle.RWKV:
            ret, indices = create_rwkv(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.PHOENIX:
            ret, indices = create_phoenix(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.LLAMA:
            ret, indices = create_llama(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATGLM:
            ret, indices = create_chatglm(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATML:
            ret, indices = create_chatml(self.settings, self.system, self.messages)
            return ret
        else:
            raise Exception("Indices not support yet.")
    
    def get_prompt(self) -> str:
        """Get the prompt for generation."""
        system_prompt = self.settings.system_template.format(system_message=self.system)
        if self.settings.sep_style == SeparatorStyle.ADD_COLON_SINGLE:
            ret, indices = create_add_colon_single(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.ADD_COLON_TWO:
            ret, indices = create_add_colon_two(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.NO_COLON_SINGLE:
            ret, indices = create_no_colon_single(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.NO_COLON_TWO:
            ret, indices = create_no_colon_two(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.ADD_NEW_LINE_SINGLE:
            ret, indices = create_add_new_line_single(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.DOLLY:
            ret, indices = create_dolly(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.RWKV:
            ret, indices = create_rwkv(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.PHOENIX:
            ret, indices = create_phoenix(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.LLAMA:
            ret, indices = create_llama(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATGLM:
            ret, indices = create_chatglm(self.settings, self.system, self.messages)
            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATML:
            ret, indices = create_chatml(self.settings, self.system, self.messages)
            return ret
        else:
            raise ValueError(f"Invalid style: {self.settings.sep_style}")

    def append_message(self, role: str, message: str):
        """Append a new message."""
        self.messages.append([role, message])

    def to_gradio_chatbot(self):
        """Convert the history to gradio chatbot format"""
        ret = []
        for i, (role, msg) in enumerate(self.messages[self.offset :]):
            if i % 2 == 0:
                ret.append([msg, None])
            else:
                ret[-1][-1] = msg
        return ret

    def to_openai_api_messages(self):
        """Convert the conversation to OpenAI chat completion format."""
        ret = [{"role": "system", "content": self.system}]

        for i, (_, msg) in enumerate(self.messages[self.offset :]):
            if i % 2 == 0:
                ret.append({"role": "user", "content": msg})
            else:
                if msg is not None:
                    ret.append({"role": "assistant", "content": msg})
        return ret

    def copy(self):
        return ConversationHistory(
            system=self.system,
            messages=[[x, y] for x, y in self.messages],
            offset=self.offset,
            settings=self.settings
        )

    def dict(self):
        return {
            "system": self.system,
            "messages": self.messages,
            "offset": self.offset,
            "settings": self.settings,
        }

