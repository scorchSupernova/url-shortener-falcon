import settings
from user_info.urls import get_router_for_user
# from authentication.urls import get_router_for_auth
from url_shortener.urls import get_router_for_url_shortener

get_router_for_user()
# get_router_for_auth()
get_router_for_url_shortener()

if __name__ == '__main__':
    from wsgiref import simple_server
    print("------: ", settings.PORT)
    httpd = simple_server.make_server('localhost', settings.PORT, settings.app)
    print("Server started at: {port}".format(port=settings.PORT),"  ", httpd.server_address)
    httpd.serve_forever()









