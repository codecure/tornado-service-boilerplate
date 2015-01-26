# coding: utf-8
import json
import httplib
from tornado.escape import json_decode
from tornado.web import RequestHandler, HTTPError
from service import __app_version__


class BaseHandler(RequestHandler):
    """Базовый класс хэндлера"""
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def set_default_headers(self):
        """Устанавливаем заголовки по умолчанию для всех handler'ов"""
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def prepare(self):
        """Преобразование тела входящих запросов в JSON"""
        if self.request.body:
            try:
                json_data = json_decode(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                raise HTTPError(status_code=400, reason=message)

    def write_json(self, obj):
        """Записываем версию приложения и время отклика в ответ
        и возвращаем JSON
        """
        obj = dict(data=obj, **dict(
            version=__app_version__, request_time=int(
                1000.0 * self.request.request_time())))  # ms

        self.write(json.dumps(obj))

    def return_status(self, status=200, msg=''):
        """Возвращает ответ с нужным статусом
        :param status: статус ответа
        :param msg: сообщение для вывода в теле ответа
        :return: None
        """
        self.clear()
        self.set_status(status, reason=httplib.responses[status])
        self.finish(msg)