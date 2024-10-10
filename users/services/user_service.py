from ..models import Users, Investment_Profiles;
from helpers import BadRequestException, ServerErrorException, INVESTMENT_PROFILES;

class UserService():
    def __init__(self):
        pass

    def create_user(self, data: dict) -> Users:
        if not (data['investment_profile_id'] in list(INVESTMENT_PROFILES.keys())):
            raise BadRequestException('Invalid investment_profile_id');

        user = Users(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            invest_profile_id=data['investment_profile_id'],
        );

        try:
            user.save();
        
            return user;
        except:
            raise ServerErrorException('Could not save user');