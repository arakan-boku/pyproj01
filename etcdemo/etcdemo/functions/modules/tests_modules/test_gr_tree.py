import unittest
from .. import make_gr_data


class TestGrTree(unittest.TestCase):

    def test_draw_data(self):
        g = make_gr_data.GrTree()
        xstr, ystr = g.draw()
        self.assertEquals(xstr[1], '2')
        self.assertEquals(ystr[1], '8')


class TestGrFern(unittest.TestCase):

    def test_draw_data(self):
        g = make_gr_data.GrFern()
        xstr, ystr = g.draw()
        self.assertEquals(xstr[2], '0')
        self.assertEquals(ystr[2], '1')
