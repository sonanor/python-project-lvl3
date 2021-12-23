from bs4 import BeautifulSoup

from page_loader.helpers import get_attribute, refer_to_hostname


def write_html_to_file(file_path: str, source_paths: list[str], soup: BeautifulSoup, url: str) -> None:
    """
    Записывает ссылки в html в пути на скаченные файлы на диске.
    :param file_path: Путь до скаченного html файла.
    :param source_paths: Список путей до скаченных файлов.
    :param soup: BeautifulSoup.
    :param url: Ссылка на сайт.
    :return:
    """
    tag_list = ['img', 'script', 'link']
    with open(file_path, 'w+') as file:
        for source in source_paths:
            for tag in tag_list:
                tag_attr = get_attribute(tag)
                for item in soup.find_all(tag):
                    arg_url = item.get(tag_attr)
                    if not arg_url or not refer_to_hostname(url, arg_url):
                        continue
                    item[tag_attr] = source
        file.write(soup.prettify())
