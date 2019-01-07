import omeroweb
from omeroweb.webclient.views import WebclientLoginView


class CustomWebclientLoginView(WebclientLoginView):

    template = "wsi/login.html"
    useragent = 'OMERO.web'


omeroweb.webclient.views.WebclientLoginView = CustomWebclientLoginView
