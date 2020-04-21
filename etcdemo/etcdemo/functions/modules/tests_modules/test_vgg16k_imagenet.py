import unittest
import base64
from django.conf import settings
from .. import vgg16_imagenet as model
import os


class TestVgg16(unittest.TestCase):

    def setUp(self):
        self.model = model.Vgg16k()
        self.datapath = getattr(settings,
                                'BASE_DIR',
                                None) + getattr(settings,
                                                'TEST_MODULES_PATH',
                                                None)

    def test_predict_from_path(self):
        a = self.model.predict_from_path(os.path.join(self.datapath, 'test.jpg'))
        self.assertEquals(a['en'], 'bassoon')
        self.assertEquals(a['jp'], 'ファゴット')
        self.assertEquals(a['pp'], '73.53%')

    def test_predict_from_base64(self):
        f = open(os.path.join(self.datapath, 'test.jpg'), 'rb').read()
        a = self.model.predict_from_base64(base64.b64encode(f))
        self.assertEquals(a['jp'], 'ファゴット')
