import os.path
from typing import Optional

import requests
from bs4 import BeautifulSoup

from page_loader.helpers import get_image_urls, is_valid_url
from page_loader.path_manager import create_html_filepath, create_image_path
from page_loader.html_writer import write_html_to_file


def download_images(image_urls: list[str], page_url: str, directory: str) -> list[str]:
    image_paths = []
    for url in image_urls:
        response = requests.get(url, stream=True)
        image_path = create_image_path(url, page_url, directory)
        dir_path = os.path.dirname(image_path)
        try:
            os.makedirs(dir_path)
        except OSError:
            pass
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        image_paths.append(image_path)
    return image_paths


def download_page(directory: str, url: str) -> Optional[str]:
    if not is_valid_url(url):
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = get_image_urls(url, soup)
    image_paths = download_images(image_urls, url, directory)
    file_path = create_html_filepath(url, directory)
    write_html_to_file(file_path, image_paths, soup)
    return file_path


