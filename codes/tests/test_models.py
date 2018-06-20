from django.test import TestCase

from ..models import PassCode, Tag


class PassCodeModelTest(TestCase):

    def test_passcode(self):
        p = PassCode.objects.create(code='1', message='123', checked=True)
        self.assertEqual(p.code, '1')
        self.assertEqual(p.message, '123')
        self.assertEqual(p.checked, True)

    def test_checked_default_false(self):
        p = PassCode.objects.create(code='2', message='456')
        self.assertEqual(p.checked, False)

    def test_to_string(self):
        p = PassCode.objects.create(code='asdafh324vbk', message='789')
        self.assertEqual(p.code, str(p))

        t = Tag.objects.create(name='测试Tag')
        self.assertEqual(t.name, str(t))
