# coding: utf-8
import os
import yaml
from service import __project_name__


def load_configuration():
    """Загрузка конфигурации по фиксированным путям и названию
    :return: словарь с текущей конфигурацией
    """
    configuration = None
    curdir = os.path.dirname(os.path.abspath(__file__))

    for loc in (os.path.join(curdir, "../config"),
                "/etc/%s/" % __project_name__):
        try:
            with open(os.path.join(loc, "config.yml")) as source:
                configuration = yaml.safe_load(source)
        except IOError:
            pass

    if not configuration:
        raise RuntimeError('Configuration file not found')

    return configuration