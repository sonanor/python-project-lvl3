import os
from tempfile import TemporaryDirectory

import pytest
from bs4 import BeautifulSoup

from page_loader.helpers import get_slugify_string, refer_to_hostname
from page_loader.html_writer import write_html_to_file
from page_loader.path_manager import create_html_filepath, create_source_path


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
     '/var/tmp/endoftheinternet-com_files/endoftheinternet-com-xkcd_book.png')
])
def test_create_image_path(image_url, page_url, directory, expected):
    assert create_source_path(image_url, page_url, directory) == expected


@pytest.mark.parametrize('url, relative_url, expected', [
    ('http://endoftheinternet.com', 'xkcd/book.png', True),
    ('http://endoftheinternet.com', 'http://endoftheinternet.com/xkcd_book.png', True),
    ('https://ru.hexlet.io/courses', 'https://cdn2.hexlet.io/assets/menu.css', False)
])
def test_refer_to_host(url, relative_url, expected):
    assert refer_to_hostname(url, relative_url) == expected


# def test_write_html_to_file():
#     source_path = ['https://ru.hexlet.io/assets/professions/nodejs.png']
#     url = 'https://ru.hexlet.io/courses/'
#     html_after = open('fixtures/after_processing_src.html').read()
#     with open('fixtures/before_processing_src.html') as html_before:
#         soup = BeautifulSoup(html_before, 'html.parser')
#         with TemporaryDirectory() as tmpdir_for_test:
#             tmpfile_for_test = os.path.join(tmpdir_for_test, 'sample.html')
#             assert write_html_to_file(tmpfile_for_test, source_path, soup, url) == html_after
