import json

from django.urls import reverse
from rest_framework import test


from ..models import PassCode, Tag


class CodesViewSetsTestCase(test.APITestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='测试标签1', weight=100)
        self.tag2 = Tag.objects.create(name='测试标签2', weight=80)
        self.code1 = PassCode.objects.create(
            code='123', message='这只是一条测试信息', checked=True
        )
        self.code1.tags.add(self.tag1)

        self.code2 = PassCode.objects.create(
            code='23333', message='这只是另一条测试信息', checked=False
        )
        self.code2.tags.add(self.tag1)
        self.code2.tags.add(self.tag2)

    def test_get_codes(self):
        url = reverse('codes-list')
        response = json.loads(self.client.get(url).content)
        self.assertEqual(response['results'][0]['id'], self.code1.id)
        self.assertEqual(response['results'][1]['id'], self.code2.id)

    def test_code_tags(self):
        url = reverse('codes-list')
        response = json.loads(self.client.get(url).content)
        self.assertEqual(response['results'][0]['tags'][0]['name'], self.tag1.name)

        # code2 有两个tag
        self.assertEqual(len(response['results'][1]['tags']), 2)
        # 权重次序
        self.assertEqual(response['results'][1]['tags'][0]['name'], self.tag1.name)
        self.assertEqual(response['results'][1]['tags'][1]['name'], self.tag2.name)

    # def test_upload_codes(self):
    #     pass
