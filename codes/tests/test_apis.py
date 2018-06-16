import json

from django.urls import reverse
from rest_framework import test


from ..models import PassCode


class CodesViewSetsTestCase(test.APITestCase):
    def setUp(self):
        self.code1 = PassCode.objects.create(
            code='123', message='这只是一条测试信息', checked=True
        )

        self.code2 = PassCode.objects.create(
            code='23333', message='这只是另一条测试信息', checked=False
        )

    def test_get_codes(self):
        url = reverse('codes-list')
        response = json.loads(self.client.get(url).content)
        self.assertEqual(response['results'][0]['id'], self.code1.id)
        self.assertEqual(response['results'][1]['id'], self.code2.id)

    # def test_upload_codes(self):
    #     pass
