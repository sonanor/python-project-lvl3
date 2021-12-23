import os
from urllib.parse import urlparse

from page_loader.helpers import get_url_extention, get_url_without_extention, get_url_without_scheme, get_slugify_string


def create_html_filepath(url: str, directory: str) -> str:
    """Генерирует путь к html файлу на диске."""
    url_without_scheme = get_url_without_scheme(url)
    formatted_path = get_slugify_string(url_without_scheme, '.html')
    return os.path.join(directory, formatted_path)


def create_image_path(image_url: str, page_url: str, directory: str) -> str:
    """Генерирует путь к файлу-изображению на диске."""
    base_url = get_slugify_string(urlparse(page_url).netloc, '_files')
    image_basename = get_url_without_extention(urlparse(image_url).path)
    image_ext = get_url_extention(image_url)
    image_path = get_slugify_string(image_basename, f'.{image_ext}')
    return os.path.join(directory, base_url, image_path)
