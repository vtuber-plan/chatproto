import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.llama import llama

class TestLlamaMethods(unittest.TestCase):
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

    SPECIAL_TAGS = [B_INST, E_INST, "<<SYS>>", "<</SYS>>"]
    UNSAFE_ERROR = "Error: special tags are not allowed as part of the prompt."

    def get_llama_prompt(self, dialogs):
        unsafe_requests = []
        prompt_tokens = []
        for dialog in dialogs:
            unsafe_requests.append(
                any([tag in msg["content"] for tag in self.SPECIAL_TAGS for msg in dialog])
            )
            if dialog[0]["role"] == "system":
                dialog = [
                    {
                        "role": dialog[1]["role"],
                        "content": self.B_SYS
                        + dialog[0]["content"]
                        + self.E_SYS
                        + dialog[1]["content"],
                    }
                ] + dialog[2:]
            assert all([msg["role"] == "user" for msg in dialog[::2]]) and all(
                [msg["role"] == "assistant" for msg in dialog[1::2]]
            ), (
                "model only supports 'system', 'user' and 'assistant' roles, "
                "starting with 'system', then 'user' and alternating (u/a/u/a/u...)"
            )
            dialog_tokens: str = "".join([
                f"{self.B_INST} {(prompt['content']).strip()} {self.E_INST} {(answer['content']).strip()} "
                for prompt, answer in zip(
                    dialog[::2],
                    dialog[1::2],
                )
            ])
            assert (
                dialog[-1]["role"] == "user"
            ), f"Last message must be from user, got {dialog[-1]['role']}"
            dialog_tokens += f"{self.B_INST} {(dialog[-1]['content']).strip()} {self.E_INST}"
            prompt_tokens.append(dialog_tokens)
        return prompt_tokens

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (llama.roles[0], "aaa"),
                (llama.roles[1], "bbb"),
                (llama.roles[0], "ccc"),
            ],
            offset=0,
            settings=llama
        )
        my_out = history.get_prompt()
        llama_out = self.get_llama_prompt([[
            {"role": "system", "content": "SYSTEM_MESSAGE"},
            {"role": llama.roles[0], "content": "aaa"},
            {"role": llama.roles[1], "content": "bbb"},
            {"role": llama.roles[0], "content": "ccc"},
        ]])[0]
        self.assertEqual(my_out, llama_out)
    
    def test_conv2(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (llama.roles[0], "aaa"),
                (llama.roles[1], "bbb"),
                (llama.roles[0], "ccc"),
                (llama.roles[1], None),
            ],
            offset=0,
            settings=llama
        )
        my_out = history.get_prompt()
        llama_out = self.get_llama_prompt([[
            {"role": "system", "content": "SYSTEM_MESSAGE"},
            {"role": llama.roles[0], "content": "aaa"},
            {"role": llama.roles[1], "content": "bbb"},
            {"role": llama.roles[0], "content": "ccc"},
        ]])[0]
        self.assertEqual(my_out, llama_out)

if __name__ == '__main__':
    unittest.main()