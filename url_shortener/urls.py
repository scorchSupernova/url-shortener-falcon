from url_shortener.url_shorten import ShortenUrlResource, ShortenUrlRedirectResource
import settings

shorten_url = ShortenUrlResource()
shorten_url_redirect = ShortenUrlRedirectResource()

def get_router_for_url_shortener():
    settings.app.add_route('/do-shorten-url', shorten_url)
    settings.app.add_route('/do-shorten-url-redirect/{url}', shorten_url_redirect)








