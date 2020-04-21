# from .modules import word2vec as w2v
from django.conf import settings
from .modules import word2vec as wv
from .modules import vgg16_imagenet as model
import re


class Demo01Functions:
    def __init__(self):
        self.basedir = getattr(settings, 'BASE_DIR', None)
        self.jabin = getattr(settings, 'JA_BIN', None)
        self.word2vec = wv.Word2Vec(self.basedir + self.jabin)

    def plus_split(self, input_text):
        return re.split(r'[\s　,\t+＋]', input_text)

    def minus_split(self, input_text):
        return re.split(r'[\s　,\t-ー]', input_text)

    def get_result(self, plusinput="", minusinput=""):
        # 半角・全角空白。一応、カンマとタブも区切りにしてみた
        pluslist = []
        minuslist = []
        pluslist = self.plus_split(plusinput)
        minuslist = self.minus_split(minusinput)
        results, expstr = self.word2vec.get_most_similar(pluslist, minuslist)
        return results, expstr


class Demo02Function:

    def __init__(self):
        self.model = model.Vgg16k()
        self.datapath = getattr(settings,
                                'BASE_DIR',
                                None) + getattr(settings,
                                                'TEST_MODULES_PATH',
                                                None)

    def img_text_replace(self, droped_base64_encoded_img):
        return re.sub('data:image/jpeg;base64,|data:image/png;base64,', '', droped_base64_encoded_img)
        """
        droped_base64_encoded_img.replace(
            'data:image/jpeg;base64,', '')
        """

    def predict_from_base64(self, droped_base64_encoded_img):
        try:
            # drag&drop後取得したテキストには余分な情報がはいっているので除去する
            # if('data:image/jpeg' in droped_base64_encoded_img):
            base64_img = self.img_text_replace(droped_base64_encoded_img)
            # else:
            #     base64_img = self.png_replace(droped_base64_encoded_img)
            return self.model.predict_from_base64(base64_img), base64_img
        except BaseException:
            return {}, ""
