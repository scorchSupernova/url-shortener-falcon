import os
import falcon

app = falcon.App()

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 8000)
SECRET_KEY = os.getenv("SECRET_KEY", "126e3ceb016272a4d7f2bc4f72263ae1cc3edc0bd91e3ca78b28bc919ce19966")

DB_DSN = os.getenv("DB_DSN", "postgresql://sajol:sajol12213@localhost:5432/falcon_db")