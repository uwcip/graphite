from django.contrib.auth.middleware import RemoteUserMiddleware
class ForwardedUserMiddleware(RemoteUserMiddleware):
    header = "HTTP_X_FORWARDED_USER"
