import factory;
from factory.faker import faker;
from helpers import INVESTMENT_PROFILES;
from .models import Investment_Profiles;
from hashlib import sha1;
import random;

class UsersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.Users';
        django_get_or_create = (
            'first_name',
            'last_name',
            'email',
            'password',
            'investment_profile_id'
        );
    

    first_name = faker.Faker().first_name();
    last_name = faker.Faker().last_name();
    email = faker.Faker().email();
    password = sha1('abc123'.encode('utf-8')).hexdigest();
    investment_profile_id = random.choice(list(INVESTMENT_PROFILES.keys()));