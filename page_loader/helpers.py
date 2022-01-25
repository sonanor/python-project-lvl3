import re
from urllib.parse import urljoin, urlparse

import validators
from validators import ValidationFailure


def create_absolute_url(domain: str, source_urls: list) -> list:
    """Создает список абсолютных путей к списку ссылок"""
    source_list = []
    for url in source_urls:
        absolute_url = urljoin(domain, urlparse(url).path)
        if is_valid_url(absolute_url):
            source_list.append(absolute_url)
    return source_list


def get_attribute(tag: str) -> str:
    if tag == 'link':
        return 'href'
    return 'src'


def refer_to_hostname(url: str, source_url) -> bool:
    url_hostname = urlparse(url).netloc
    relative_url_hostname = urlparse(source_url).netloc
    return not relative_url_hostname or url_hostname == relative_url_hostname


def is_valid_url(url):
    return validators.url(url) is True


def test_is_valid_url():
    url = 'http://endm'
    # raise ValueError
    assert is_valid_url(url) is False


def get_url_extention(url: str) -> str:
    url = url.partition('?')[0]
    return url.rpartition('.')[-1]


def get_url_without_extention(url: str) -> str:
    url = url.partition('?')[0]
    return url.rpartition('.')[0]


def get_url_without_scheme(url: str) -> str:
    parsed_url = urlparse(url)
    scheme = f'{parsed_url.scheme}://'
    return parsed_url.geturl().replace(scheme, '')


def get_slugify_string(url: str, suffix: str = '') -> str:
    """Возвращает slugify строку с суффиксом."""
    formatted_url = re.sub('[./]', '-', url) + suffix
    return formatted_url.removeprefix('-')
