import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.conversation.models.baichuan import baichuan

class TestBaiChuanMethods(unittest.TestCase):

    def test_conv(self):
        history = ConversationHistory(
            "SYSTEM_MESSAGE",
            messages=[
                (baichuan.roles[0], "aaa"),
                (baichuan.roles[1], "bbb"),
            ],
            offset=0,
            settings=baichuan
        )
        self.assertEqual(history.get_prompt(), "SYSTEM_MESSAGE<reserved_102>aaa<reserved_103>bbb")

if __name__ == '__main__':
    unittest.main()
