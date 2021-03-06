from __future__ import absolute_import

from pystat.tests.base import TestCase
from pystat.timer import Timer


class TestTimer(TestCase):

    def setUp(self):
        super(TestTimer, self).setUp()
        self.timer = Timer()

    def test_add(self):
        self.timer.add(1.0)
        self.assertEqual(1, int(self.timer))
        self.timer.add(1.0)
        self.assertEqual(2, int(self.timer))

    def test_add_sample(self):
        self.timer.add(5)
        self.assertEqual(5, int(self.timer))

    def test_iadd(self):
        self.timer += 1
        self.assertEqual(1, int(self.timer))

    def test_count(self):
        self.timer.add(1.0)
        self.timer.add(1.0)
        self.assertEqual(2, len(self.timer))

    def test_query(self):
        self.timer.add(1.0)
        self.timer.add(1.0)
        self.timer.add(2.0)
        self.assertEqual(1.0, self.timer.query(0.5))
        self.assertEqual(2.0, self.timer.query(0.95))
