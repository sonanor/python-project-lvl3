import re
from typing import Any
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


# def is_valid_image_url(url: str) -> bool:
#     return url.endswith('.png') or url.endswith('.jpg')


# def get_image_urls(url: str, soup: BeautifulSoup) -> list[str]:
#     images_list = []
#     for img in soup.find_all('img'):
#         img_url = img.attrs.get('src')
#         if not img_url:
#             continue
#         img_url = urljoin(url, img_url)
#         if is_valid_url(img_url) and is_valid_image_url(img_url):
#             images_list.append(img_url)
#     return images_list


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
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


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
