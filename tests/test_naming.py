import pytest

from page_loader.helpers import get_slugify_string
from page_loader.path_manager import create_html_filepath, create_image_path


@pytest.mark.parametrize('url, directory, expected', [
    ('http://endoftheinternet.com', '/var/tmp', '/var/tmp/endoftheinternet-com.html'),
    ('https://ru.hexlet.io/courses', '/var/tmp', '/var/tmp/ru-hexlet-io-courses.html')
])
def test_create_html_filepath(url, directory, expected):
    assert create_html_filepath(url, directory) == expected


@pytest.mark.parametrize('url, suffix, expected', [
    ('endoftheinternet.com', '_files', 'endoftheinternet-com_files'),
    ('ru.hexlet.io/courses', '_files', 'ru-hexlet-io-courses_files'),
    ('/assets/professions/nodejs', '.png', 'assets-professions-nodejs.png')
])
def test_slugify_string(url, suffix, expected):
    assert get_slugify_string(url, suffix) == expected


@pytest.mark.parametrize('image_url, page_url, directory, expected', [
    ('http://endoftheinternet.com/xkcd_book.png',
     'http://endoftheinternet.com',
     '/var/tmp/',
     '/var/tmp/endoftheinternet-com_files/xkcd_book.png')
])
def test_create_image_path(image_url, page_url, directory, expected):
    assert create_image_path(image_url, page_url, directory) == expected
