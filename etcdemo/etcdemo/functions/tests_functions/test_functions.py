import unittest
import base64
import os
from django.conf import settings
from .. import functions as func

"""
モジュール機能テストは各UnitTestで行う。
functionで新規追加したロジックがなければ、おちない確認がとれれば良い。
"""


class TestDemo01Function(unittest.TestCase):

    def test_not_exception(self):
        try:
            f = func.Demo01Functions()
            plusinput = ""
            minusinput = ""
            results, expstr = f.get_result(plusinput, minusinput)
            self.assertTrue(True)
        except BaseException:
            self.assertFalse(False)

    def test_plus_split(self):
        f = func.Demo01Functions()
        plist = f.plus_split("日本＋人生　木")
        self.assertEquals(plist, ['日本', '人生', '木'])

    def test_minus_split(self):
        f = func.Demo01Functions()
        plist = f.minus_split("日本ー人生　木")
        self.assertEquals(plist, ['日本', '人生', '木'])


class TestDemo02Functions(unittest.TestCase):

    def test_img_text_replace(self):
        f = func.Demo02Function()
        a = f.img_text_replace("data:image/jpeg;base64,0A0DFF")
        self.assertEquals(a, "0A0DFF")

    def test_png_replace(self):
        f = func.Demo02Function()
        a = f.img_text_replace("data:image/png;base64,0A0DFF")
        self.assertEquals(a, "0A0DFF")

    def test_not_exception(self):
        try:
            model = func.Demo02Function()
            datapath = getattr(settings,
                               'BASE_DIR',
                               None) + getattr(settings,
                                               'TEST_MODULES_PATH',
                                               None)
            f = open(os.path.join(datapath, 'test.jpg'), 'rb').read()
            model.predict_from_base64(base64.b64encode(f))
            self.assertTrue(True)
        except BaseException:
            self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
