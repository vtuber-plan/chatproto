import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.openbuddy import openbuddy


class TestOpenbuddyMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (openbuddy.roles[0], "aaa"),
                (openbuddy.roles[1], "bbb"),
            ],
            offset=0,
            settings=openbuddy
        )
        self.assertEqual(history.get_prompt(), """SYSTEM_MESSAGE

User: aaa
Assistant: bbb
""")

if __name__ == '__main__':
    unittest.main()
