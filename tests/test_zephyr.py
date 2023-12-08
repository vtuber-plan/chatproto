import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.zephyr import zephyr


class TestZephyrMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (zephyr.roles[0], "aaa"),
                (zephyr.roles[1], "bbb"),
                (zephyr.roles[0], "ccc"),
                (zephyr.roles[1], None),
            ],
            offset=0,
            settings=zephyr
        )
        self.assertEqual(history.get_prompt(), """<|system|>
SYSTEM_MESSAGE</s>
<|user|>
aaa</s>
<|assistant|>
bbb</s>
<|user|>
ccc</s>
<|assistant|>
""")

if __name__ == '__main__':
    unittest.main()
