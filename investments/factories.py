import factory;
from factory.faker import faker;
from .models import Asset_Types;
from helpers import ASSET_TYPES;
import random;

class AssetsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'investments.Assets';
        django_get_or_create = (
            'asset_type_id',
            'asset_name'
        );
    

    asset_name = 'IBOV11';
    asset_type_id = random.choice(list(ASSET_TYPES.keys()));