# coding: utf-8
from functools import wraps
from tornado.web import HTTPError
from tornado.escape import url_unescape


def token_check(f):
    """Декоратор для авторизации по токену, пришедшему в теле
    запроса или в GET параметрах

    :param f: декорируемая функция
    :return: результат выполнения декорируемой функции
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        handler_obj = args[0]

        token = (handler_obj.get_query_argument(
            'token', '') or handler_obj.request.arguments.get('token', ''))
        token = url_unescape(token)

        if not token or (token and token != handler_obj.application.conf[
                'app']['token']):
            raise HTTPError(status_code=401, reason='Not authorized')

        result = f(*args, **kwargs)
        return result
    return decorated_function
