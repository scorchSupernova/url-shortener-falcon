from .user_api import UserResource
import settings

user = UserResource()

def get_router_for_user():
    settings.app.add_route('/create-user', user)








