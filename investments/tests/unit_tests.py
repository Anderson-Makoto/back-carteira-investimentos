from django.test import TestCase;
from investments.models import User_Investments;
from users.models import Users;
from investments.models import Assets;
from users.factories import UsersFactory;
from investments.factories import AssetsFactory;
from rest_framework import status;
import datetime;
from django.core.management import call_command;

class InvestmentsTest(TestCase):
    user: Users = None;
    asset: Assets = None;
    USER_PASSWORD = 'abc123';

    def setUp(self):
        call_command('seed_db');
        self.user = UsersFactory(password=self.USER_PASSWORD);
        self.asset = AssetsFactory();

        return super().setUp();

    def test_save_user_investment(self):
        current_timestamp = datetime.datetime.now().timestamp();

        request_data = {
            'user_id': self.user.id,
            'capital': 10000,
            'assets_id': self.asset.id,
            'date_time': current_timestamp,
            'is_buying': True,
            'amount': 20,
        };

        response = self.client.post('/investments/save_investment/', data=request_data);

        self.assertEqual(response.status_code, status.HTTP_201_CREATED);
        self.assertEqual(User_Investments.objects.count(), 1);

        user_investment = User_Investments.objects.last();

        self.assertEqual(user_investment.user_id, self.user.id);
        self.assertEqual(user_investment.assets_id, self.asset.id);
        self.assertEqual(user_investment.capital, request_data['capital']);
        self.assertEqual(float(user_investment.date_time), current_timestamp);
        self.assertEqual(user_investment.is_buying, request_data['is_buying']);
        self.assertEqual(user_investment.amount, request_data['amount']);

    def test_save_user_investment_fails(self):
        current_timestamp = datetime.datetime.now().timestamp();

        invalid_user_id = self.user.id + 1;

        request_data = {
            'user_id': invalid_user_id,
            'capital': 10000,
            'assets_id': self.asset.id,
            'date_time': current_timestamp,
            'is_buying': True,
            'amount': 20,
        };

        response = self.client.post('/investments/save_investment/', data=request_data);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);
        self.assertEqual(User_Investments.objects.count(), 0);

        invalid_asset_id = self.asset.id + 1;

        request_data = {
            'user_id': self.user.id,
            'capital': 10000,
            'assets_id': invalid_asset_id,
            'date_time': current_timestamp,
            'is_buying': True,
            'amount': 20,
        };

        response = self.client.post('/investments/save_investment/', data=request_data);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);
        self.assertEqual(User_Investments.objects.count(), 0);