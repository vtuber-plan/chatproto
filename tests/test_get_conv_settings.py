import unittest

from chatproto.conversation.history import ConversationHistory
from chatproto.registry import get_conv_settings

class TestGetConvSettingsMethods(unittest.TestCase):

    def test_conv(self):
        baichuan = get_conv_settings("baichuan")
        self.assertEqual(baichuan.name, "baichuan")

        llama = get_conv_settings("llama")
        self.assertEqual(llama.name, "llama")

if __name__ == '__main__':
    unittest.main()
