from bs4 import BeautifulSoup


def write_html_to_file(file_path: str, image_filepaths: list[str], soup: BeautifulSoup) -> None:
    with open(file_path, 'w+') as file:
        for img_path in image_filepaths:
            for img in soup.find_all('img'):
                img['src'] = img_path
        file.write(soup.prettify())

