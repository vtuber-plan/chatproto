import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.baichuan import baichuan2


class TestBaiChuanMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (baichuan2.roles[0], "aaa"),
                (baichuan2.roles[1], "bbb"),
            ],
            offset=0,
            settings=baichuan2
        )
        self.assertEqual(history.get_prompt(), "SYSTEM_MESSAGE<reserved_106>aaa<reserved_107>bbb")

if __name__ == '__main__':
    unittest.main()
