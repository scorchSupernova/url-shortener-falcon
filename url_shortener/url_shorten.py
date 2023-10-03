import hashlib
from authentication.generate_token import verify_token
import falcon
import json

from db_config.db_con import get_session
from .models import UrlShortener
from user_info.models import User
from sqlalchemy.exc import IntegrityError

class ShortenUrlResource:
    def __init__(self):
        self.session = get_session()

    def on_post(self, req, resp):
        authorization = req.get_header('Authorization', None)
        if authorization is not None:
            authorization_token = authorization.split(' ')
            payload_data = req.media
            if len(authorization_token) >= 2:
                token = authorization_token[1]
                is_valid, username, email = verify_token(token)
                if is_valid:
                    try:
                        long_url = payload_data.get('long_url')
                        hashed_url = hashlib.sha256()
                        hashed_url.update(long_url.encode('utf-8'))
                        decoded_url_string = hashed_url.hexdigest()[:8].encode('utf-8').decode('utf-8')
                        short_url = ''.join(url for url in decoded_url_string if url.isalnum())
                        user_id = User().get_user_id(username, email).id
                        url_shortener_obj = UrlShortener(user_id=user_id, actual_url=long_url, short_url=short_url)
                        self.session.add(url_shortener_obj)
                        self.session.commit()
                        resp.status = falcon.HTTP_200
                        resp.body = json.dumps({"message": "Request Successful", "code": 200, "data": {"long_url": long_url ,"short_url": short_url}})
                    except IntegrityError as e:
                        print(e)
                        self.session.rollback()

                else:
                    resp.status = falcon.HTTP_400
                    resp.body = json.dumps({"code": 400, "message": "Signature has expired", "data": []})

            else:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({"code": 400, "message": "Token is not valid", "data": []})
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"code": 400, "message": "Please provide authorization token", "data": []})

class ShortenUrlRedirectResource:
    def __init__(self):
        self.session = get_session()

    def on_get(self, req, resp, url):
        url_shortener = self.session.query(UrlShortener).filter_by(short_url=url).first()
        authorization = req.get_header('Authorization', None)
        if authorization is not None:
            authorization_token = authorization.split(' ')
            if len(authorization_token) >= 2:
                token = authorization_token[1]
                is_valid, _, _ = verify_token(token)
                if is_valid:
                    if url_shortener:
                        resp.status = falcon.HTTP_200
                        resp.body = json.dumps({"code": 200, "message": "Request Successful", "data": {"long_url": url_shortener.actual_url, "short_url": url}})
                    else:
                        resp.status = falcon.HTTP_404
                        resp.body = json.dumps({"code": 404, "message": "URL not found", "data": []})
                else:
                    resp.status = falcon.HTTP_400
                    resp.body = json.dumps({"code": 400, "message": "Signature has expired", "data": []})
            else:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({"code": 400, "message": "Token is not valid", "data": []})
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"code": 400, "message": "Please provide authorization token", "data": []})



