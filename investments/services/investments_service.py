from ..models import User_Investments, Assets;
from users.models import Users;
from helpers import BadRequestException, ServerErrorException;

class InvestmentsService():
    def __init__(self):
        None;

    def create_investment(self, data: dict) -> User_Investments:
        user_exists = Users.objects.filter(id=data['user_id']).exists();
        asset_exists = Assets.objects.filter(id=data['assets_id']).exists();

        if (not user_exists) or (not asset_exists):
            raise BadRequestException("Invalid user or\\and asset");

        user_investment = User_Investments(
            user_id=data['user_id'],
            capital=data['capital'],
            assets_id=data['assets_id'],
            date_time=data['date_time'],
            is_buying=data['is_buying'],
            amount=data['amount']
        );

        try:
            user_investment.save();
        
            return user_investment;
        except:
            raise ServerErrorException('Could not save user investment');