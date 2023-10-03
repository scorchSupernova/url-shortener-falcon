import jwt
from datetime import datetime, timedelta
import settings

def generate_token(data):
    secret_key = settings.SECRET_KEY
    payload = {
        "username": data.get("username"),
        "email": data.get("email"),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return jwt_token


def verify_token(token: str):
    secret_key = settings.SECRET_KEY
    try:
        cur_datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        if 'exp' in payload:
            expiration_datetime = datetime.utcfromtimestamp(payload['exp'])
            print(expiration_datetime," ", cur_datetime)
            if str(expiration_datetime) >= cur_datetime:
                return True, payload['username'], payload['email']
            else:
                return False, None, None

    except jwt.exceptions.InvalidTokenError as e:
        print(e)
        return False, None, None

if __name__ == '__main__':
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNham9sc3MiLCJlbWFpbCI6InNham9sQGdtYWlsLmNvbSIsImV4cCI6MTY5NjI0NzkxNX0.y5gC566VyUjOxE29d2z_EkaQ4vCc87nkO-Udc9o5GjM"
    print(token)
    verify_token(token)


