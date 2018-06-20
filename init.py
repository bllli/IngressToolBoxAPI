"""初始化道具类别 道具详情"""
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'IngressToolBoxAPI.settings'
    django.setup()

    from codes.models import Item, ItemType
    item_tuples = [
        ('Capsule', 'Capsule', [Item.RARITY_COMMON], None),
        ('Capsule', 'Key Locker', [Item.RARITY_VERY_RARE], None),
        ('Capsule', 'MUFG Capsule', [Item.RARITY_VERY_RARE], None),
        ('Capsule', 'Quantum Capsule', [Item.RARITY_VERY_RARE], None),
        ('Mod', 'Force Amp', [Item.RARITY_RARE], None),
        ('Mod', 'Heat Sink', Item.RARITY_LIST, None),
        ('Mod', 'Link Amp', [Item.RARITY_RARE, Item.RARITY_VERY_RARE], None),
        ('Mod', 'SoftBank Ultra Link', [Item.RARITY_VERY_RARE], None),
        ('Mod', 'Multi-hack', Item.RARITY_LIST, None),
        ('Mod', 'Portal Shield', Item.RARITY_LIST, None),
        ('Mod', 'AXA Shield', [Item.RARITY_VERY_RARE], None),
        ('Mod', 'Aegis Shield', [Item.RARITY_VERY_RARE], None),
        ('Mod', 'Turret', [Item.RARITY_RARE], None),
        ('Media', 'Media', [Item.RARITY_COMMON], None),
        ('Portal Key', 'Portal Key', [Item.RARITY_COMMON], None),
        ('Power Cube', 'Power Cube', [Item.RARITY_COMMON], range(1, 9)),
        ('Power Cube', 'Lawson Power Cube', [Item.RARITY_VERY_RARE], None),
        ('Power Cube', 'Circle-K Power Cube', [Item.RARITY_VERY_RARE], None),
        ('Resonator', 'Resonator', [Item.RARITY_COMMON], range(1, 9)),
    ]

    for item_type, item_name, rarity_list, level_list in item_tuples:
        item_type = ItemType.objects.get_or_create(name=item_type)[0]
        if level_list:
            for level in level_list:
                for rarity in rarity_list:
                    Item.objects.get_or_create(item_type=item_type, name=item_name, rarity=rarity, level=level)
        else:
            for rarity in rarity_list:
                Item.objects.get_or_create(item_type=item_type, name=item_name, rarity=rarity)
