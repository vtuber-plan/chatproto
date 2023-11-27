import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.qwen import qwen

class TestQwenMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (qwen.roles[0], "aaa"),
                (qwen.roles[1], "bbb"),
            ],
            offset=0,
            settings=qwen
        )
        self.assertEqual(history.get_prompt(), """<|im_start|>system
SYSTEM_MESSAGE<|im_end|>
<|im_start|>user
aaa<|im_end|>
<|im_start|>assistant
bbb<|im_end|>
""")

if __name__ == '__main__':
    unittest.main()
