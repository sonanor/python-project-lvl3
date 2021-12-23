from page_loader.downloader import download_page
from page_loader.path_manager import create_html_filepath
from page_loader.cli import get_args


def main():
    args = get_args()
    html_path = download_page(args.output, args.url)
    return html_path


if __name__ == '__main__':
    main()
