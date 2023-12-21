
from typing import List, Tuple
import dataclasses

from .settings import ConversationSettings, SeparatorStyle

def create_system_prompt(settings: ConversationSettings, system: str) -> str:
    system_prompt = settings.system_template.format(system_message=system)
    return system_prompt

def create_add_colon_single(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

def create_add_colon_two(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

def create_no_colon_single(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

def create_no_colon_two(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

def create_add_new_line_single(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

def create_dolly(settings: ConversationSettings, system: str, messages: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[int, int]]]:
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

@dataclasses.dataclass
class ConversationHistory:
    """A class that keeps all conversation history."""

    # System prompts
    system: str
    # All messages
    messages: List[Tuple[str, str]]
    # Offset of few shot examples
    offset: int

    settings: ConversationSettings

    def get_prompt_and_indices(self) -> Tuple[str, List[Tuple[int, int]]]:
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
            ret = system_prompt + self.settings.sep
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += (
                        role
                        + ": "
                        + message.replace("\r\n", "\n").replace("\n\n", "\n")
                    )
                    ret += "\n\n"
                else:
                    ret += role + ":"
            return ret
        elif self.settings.sep_style == SeparatorStyle.PHOENIX:
            ret = system_prompt
            for role, message in self.messages:
                if message:
                    ret += role + ": " + "<s>" + message + "</s>"
                else:
                    ret += role + ": " + "<s>"
            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATGLM:
            if system_prompt:
                ret = system_prompt + self.settings.sep
            else:
                ret = ""
            for i, (role, message) in enumerate(self.messages):
                if message:
                    if i % 2 == 0:
                        ret += f"[Round {i+1}]\n\n"
                    ret += role + "：" + message + self.settings.sep
                else:
                    ret += role + "："
            return ret
        elif self.settings.sep_style == SeparatorStyle.LLAMA:
            B_INST, E_INST = "[INST]", "[/INST]"
            if system_prompt:
                ret = system_prompt + self.settings.sep
            else:
                ret = ""
            
            if self.messages[0][0] == "system":
                self.messages.pop(0)
            for i, (role, message) in enumerate(self.messages):
                if i % 2 == 0:
                    inst = B_INST + " "
                else:
                    inst = E_INST + " "
                if i == 0:
                    inst = ""
                if message:
                    if i % 2 == 0:
                        ret += inst + message.strip() + " "
                    else:
                        ret += inst + message.strip() + " "
                    if i == len(self.messages) - 1:
                        ret += E_INST
                else:
                    ret += E_INST

            return ret
        elif self.settings.sep_style == SeparatorStyle.CHATLM:
            im_start, im_end = "<|im_start|>", "<|im_end|>"
            ret = system_prompt + self.settings.sep

            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += im_start + role + "\n" + message + im_end + self.settings.sep
                else:
                    ret += im_start + role + "\n"
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

