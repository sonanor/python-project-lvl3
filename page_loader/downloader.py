import re
import requests
import os


def create_filepath_output(url, directory):
    address = url.split('//')[1]
    spited_words_in_adress = re.split(r'[^a-zA-Z0-9]', address)
    formatted_adress = '-'.join(spited_words_in_adress) + '.html'
    result = os.path.join(directory, formatted_adress)
    return result


def download(directory, url):
    response = requests.get(url)
    file_path = create_filepath_output(url, directory)
    with open(file_path, 'w+') as file:
        file.write(response.text)
    return file_path
