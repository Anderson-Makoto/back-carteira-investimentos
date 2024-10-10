from django.test import TestCase;
from investments.models import User_Investments;
from users.models import Users;
from investments.models import Assets;
from users.factories import UsersFactory;
from investments.factories import AssetsFactory;
from rest_framework import status;
import datetime;

class InvestmentsTest(TestCase):
    user: Users = None;
    asset: Assets = None;
    USER_PASSWORD = 'abc123';

    def setUp(self):
        self.user = UsersFactory(password=self.USER_PASSWORD);
        self.asset = AssetsFactory();

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