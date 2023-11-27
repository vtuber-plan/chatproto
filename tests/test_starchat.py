import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.starchat import starchat

class TestStarChatMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (starchat.roles[0], "aaa"),
                (starchat.roles[1], "bbb"),
            ],
            offset=0,
            settings=starchat
        )
        self.assertEqual(history.get_prompt(), "<|system|>\nSYSTEM_MESSAGE<|end|>\n<|user|>\naaa<|end|>\n<|assistant|>\nbbb<|end|>\n")
    
    def test_conv_question(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (starchat.roles[0], "aaa"),
                (starchat.roles[1], None),
            ],
            offset=0,
            settings=starchat
        )
        self.assertEqual(history.get_prompt(), "<|system|>\nSYSTEM_MESSAGE<|end|>\n<|user|>\naaa<|end|>\n<|assistant|>\n")


if __name__ == '__main__':
    unittest.main()
