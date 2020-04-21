import gensim


class Word2Vec:
    def __init__(self, dicpath):
        self.model = gensim.models.Word2Vec.load(dicpath)

    def get_most_similar(self, plus_list, minus_list):
        exp_str = ''
        plus = []
        try:
            for p in plus_list:
                if p in self.model.wv.vocab:
                    plus.append(p)
            minus = []
            for m in minus_list:
                if m in self.model.wv.vocab:
                    minus.append(m)
            if not minus:
                if not plus:
                    exp_str = ''
                    result = [('辞書に存在する単語がありません。', 0.00000000)]
                else:
                    exp_str = self.__exp_str(plus, '+')
                    result = self.model.most_similar(positive=plus)
            else:
                if not plus:
                    exp_str = self.__exp_str(minus, '-')
                    result = self.model.most_similar(negative=minus)
                else:
                    exp_str = self.__exp_str(plus, '+') + '-' + self.__exp_str(minus, '-')
                    result = self.model.most_similar(
                        positive=plus, negative=minus)
        except BaseException:
            exp_str = ''
            result = [('処理中にエラーが発生しました。', 0.00000000)]
        return result, exp_str
    
    def __exp_str(self, p_list, dmtr):
        st = ''
        for i, p in enumerate(p_list):
            if i == 0:
                st = p
            else:
                st = st + str(dmtr) + p
        return st
