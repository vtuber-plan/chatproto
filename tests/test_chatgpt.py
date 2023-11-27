import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.chatgpt import chatgpt

class TestChatGPTMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (chatgpt.roles[0], "aaa"),
                (chatgpt.roles[1], "bbb"),
            ],
            offset=0,
            settings=chatgpt
        )
        self.assertEqual(history.get_prompt(), "SYSTEM_MESSAGE\n### user: aaa\n### assistant: bbb\n### ")

if __name__ == '__main__':
    unittest.main()
