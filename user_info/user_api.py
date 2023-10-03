import json

import falcon
from db_config.db_con import get_session
from .models import User
from sqlalchemy.exc import IntegrityError
from authentication.generate_token import generate_token
import logging
from authentication.models import Authentication

logger = logging.getLogger(__name__)

class UserResource:
    def __init__(self):
        self.session = get_session()

    def on_post(self, req, resp):
        req_data = json.loads(req.bounded_stream.read().decode('utf-8'))
        logger.debug("Data getting done from request....")
        new_user = User(username=req_data.get('username'), email=req_data.get('email'))
        try:
            payload = {
                "username": req_data.get("username"),
                "email": req_data.get("email")
            }
            gen_token = generate_token(payload)
            logger.debug("Token generation done successfully.....")
            token_model = Authentication(user=new_user, token=gen_token)
            self.session.add_all([new_user, token_model])
            self.session.commit()
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({"message": "Request Successful", "code": 200, "data": {"token": gen_token}})
        except IntegrityError as e:
            print(e)
            logger.error(e)
            self.session.rollback()
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"message": "Please provide necessary information!!", "code": falcon.HTTP_400})


