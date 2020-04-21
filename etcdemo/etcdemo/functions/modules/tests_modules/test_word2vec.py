import unittest
from django.conf import settings
from .. import word2vec as wv


class TestWord2Vec(unittest.TestCase):

    def setUp(self):
        self.basedir = getattr(settings, 'BASE_DIR', None)
        self.jabin = getattr(settings, 'JA_BIN', None)
        self.word2vec = wv.Word2Vec(self.basedir + self.jabin)

    def test_not_match(self):
        pluslist = []
        minuslist = []
        results, expstr = self.word2vec.get_most_similar(pluslist, minuslist)
        self.assertEqual(results, [('辞書に存在する単語がありません。', 0.0)])
        self.assertEqual(expstr, '')

    def test_plus_only(self):
        pluslist = ['日本']
        minuslist = []
        results, expstr = self.word2vec.get_most_similar(pluslist, minuslist)
        self.assertEqual(results[0][0], 'ドイツ')
        self.assertEqual(expstr, '日本')

    def test_minus_only(self):
        pluslist = []
        minuslist = ['日本']
        results, expstr = self.word2vec.get_most_similar(pluslist, minuslist)
        self.assertEqual(results[0][0], '三橋')
        self.assertEqual(expstr, '日本')

    def test_plus_minus(self):
        pluslist = ['日本']
        minuslist = ['知性']
        results, expstr = self.word2vec.get_most_similar(pluslist, minuslist)
        self.assertEqual(results[0][0], '東京')
        self.assertEqual(expstr, '日本-知性')

    def test_exception(self):
        results, expstr = self.word2vec.get_most_similar(None, None)
        self.assertEqual(results, [('処理中にエラーが発生しました。', 0.00000000)])
        self.assertEqual(expstr, '')


if __name__ == '__main__':
    unittest.main()
