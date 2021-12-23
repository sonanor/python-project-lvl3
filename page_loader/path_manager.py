import os
from urllib.parse import urlparse

from page_loader.helpers import get_url_extention, get_url_without_extention, get_url_without_scheme, get_slugify_string


def create_html_filepath(url: str, directory: str) -> str:
    """Генерирует путь к html файлу на диске."""
    url_without_scheme = get_url_without_scheme(url)
    formatted_path = get_slugify_string(url_without_scheme, '.html')
    return os.path.join(directory, formatted_path)


def create_source_path(file_url: str, page_url: str, directory: str) -> str:
    """Генерирует путь к файлу из html на диске."""
    if file_url == page_url:
        return get_slugify_string(get_url_without_scheme(page_url))
    base_url = get_slugify_string(get_url_without_scheme(page_url), '_files')  # ru-hexlet-io-courses_files
    file_basename = get_url_without_extention(get_url_without_scheme(file_url))  # lessons.png
    file_ext = get_url_extention(file_url)
    file_path = get_slugify_string(file_basename, f'.{file_ext}')
    return os.path.join(directory, base_url, file_path)
