import os
from logging import getLogger

import requests
from bs4 import BeautifulSoup
from requests import Response

from page_loader.helpers import get_attribute, refer_to_hostname
from page_loader.path_manager import create_source_path

logger = getLogger(__name__)


def download_additional_sources(source_urls: list[str], page_url: str, directory: str) -> list[str]:
    downloaded_source_paths = []
    for url in source_urls:
        response = requests.get(url, stream=True)
        file_path = create_source_path(url, page_url, directory)
        if url == page_url:
            continue
        dir_path = os.path.dirname(file_path)
        try:
            os.makedirs(dir_path)
        except OSError:
            pass
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        downloaded_source_paths.append(file_path)
    return downloaded_source_paths


def parse_html(response: Response, url: str) -> list[str]:
    """Парсит html и генерирует список ссылок в тегах img, script, link
    относящихся к домену (поддоемну)."""
    tag_list = ['img', 'script', 'link']
    source_list = []
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in tag_list:
        tag_attr = get_attribute(tag)
        for item in soup.find_all(tag):
            tag_url = item.get(tag_attr)
            if not tag_url or not refer_to_hostname(url, tag_url):
                continue
            source_list.append(tag_url)
    logger.debug(f'Created list of sources: {source_list}')
    return source_list
