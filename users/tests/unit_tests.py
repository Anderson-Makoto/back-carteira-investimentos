from django.test import TestCase;
from investments.models import User_Investments;
from users.models import Users;
from investments.models import Assets;
from users.factories import UsersFactory;
from investments.factories import AssetsFactory;
from rest_framework import status;
from django.core.management import call_command;
from hashlib import sha1;
from helpers import INVESTMENT_PROFILES;

class UsersTest(TestCase):

    def setUp(self):
        call_command('seed_db');

        return super().setUp();

    def test_save_user_should_be_successful(self):
        hashed_pass = sha1('abc123'.encode('utf-8')).hexdigest()
        request_data = {
            'first_name': 'test',
            'last_name': 'last',
            'email': 'email@email.com',
            'password': hashed_pass,
            'investment_profile_id': 
        };

        response = self.client.post('/users/save_users/', data=request_data);

        self.assertEqual(response.status_code, status.HTTP_201_CREATED);
        self.assertEqual(User_Investments.objects.count(), 1);

        user_investment = User_Investments.objects.last();

        self.assertEqual(user_investment.user_id, self.user.id);
        self.assertEqual(user_investment.assets_id, self.asset.id);
        self.assertEqual(user_investment.capital, request_data['capital']);
        self.assertEqual(float(user_investment.date_time), current_timestamp);
        self.assertEqual(user_investment.is_buying, request_data['is_buying']);
        self.assertEqual(user_investment.amount, request_data['amount']);