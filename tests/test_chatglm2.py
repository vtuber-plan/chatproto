import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.chatglm import chatglm2

class TestChatGLMMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (chatglm2.roles[0], "aaa"),
                (chatglm2.roles[1], "bbb"),
            ],
            offset=0,
            settings=chatglm2
        )
        self.assertEqual(history.get_prompt(), "SYSTEM_MESSAGE\n\n[Round 1]\n\n问：aaa\n\n答：bbb\n\n")

if __name__ == '__main__':
    unittest.main()
