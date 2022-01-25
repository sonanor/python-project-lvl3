from logging import getLogger
from typing import Optional

import requests
from bs4 import BeautifulSoup

from page_loader.helpers import is_valid_url, create_absolute_url
from page_loader.html_writer import write_html_to_file
from page_loader.path_manager import create_html_filepath
from page_loader.resources_download import download_additional_sources, parse_html

logger = getLogger(__name__)


def download_page(directory: str, url: str) -> Optional[str]:
    # logger = logging.getLogger('page_loader')
    """Downloads webpage and it's available resources."""
    if not is_valid_url(url):
        logger.error('URL is not valid')
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    source_raw_urls = parse_html(response, url)
    source_urls = create_absolute_url(url, source_raw_urls)
    source_paths = download_additional_sources(source_urls, url, directory)
    file_path = create_html_filepath(url, directory)
    write_html_to_file(file_path, source_paths, soup, url)
    return file_path
