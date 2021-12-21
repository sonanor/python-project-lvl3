from page_loader.downloader import download


def main():
    import argparse
    import os

    parser = argparse.ArgumentParser(description='Page-loader')
    parser.add_argument('-o', '--output', dest='output')
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    if not args.output:
        args.output = os.getcwd()
    result_path = download(args.output, args.url)
    return result_path


if __name__ == '__main__':
    main()
