from django.test import TestCase

from app.calc import add,subs

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3,8),11)

    def test_subs_number(self):
        self.assertEqual(subs(5,11),6)