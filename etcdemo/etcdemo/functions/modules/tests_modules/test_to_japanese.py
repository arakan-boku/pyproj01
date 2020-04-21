import unittest
from .. import to_japanese_ilsvrc2012 as toj


class TestToj(unittest.TestCase):

    def setUp(self):
        self.t = toj.Ilsvrc2012Japanese()

    def test_ok(self):
        a = self.t.convert('dugong')
        self.assertEquals(a, 'ジュゴン')

    def test_ng(self):
        a = self.t.convert('xxxxxxx')
        self.assertEquals(a, '一致するキーがありません')
