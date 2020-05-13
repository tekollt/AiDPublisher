import os
import json
import configparser
import requests

from datetime import date

default_directory = os.path.dirname(os.path.realpath(__file__))


def find_todays_filename():
    prefix = "AD"
    today = date.today()
    suffix = today.strftime("%y%m%d")
    filename = f"{prefix}{suffix}.pdf"
    return filename


def download_report(folder, filename):
    try:
        url = "https://www.dnb.no/portalfront/nedlast/no/markets/analyser-rapporter/norske/aksjemorgen/" + filename
        # print("downloading " + url)
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        return None, e.__str__()

    with open(folder + "/" + filename, 'wb') as f:
        f.write(resp.content)

    with open(folder + "/" + "AiDPublisher.pdf", 'wb') as f:
            f.write(resp.content)
    return resp.content


def main():
    config_file = default_directory + "/AiDPublisher.ini"
    script_file = default_directory + "/AiDPublisher.cmd"

    if not os.path.exists(script_file):
        with open(script_file, 'w') as file:
            file.write("@echo off \n")
            file.write("cd " + default_directory + "\n")
            file.write("AiDPublisher.exe \n")

    if os.path.exists(config_file):
        # print("reading config file")
        config = configparser.ConfigParser()
        config.sections()
        config.read(config_file)

        save_path = config.get('DEFAULT', 'path').replace('\\', '/')

    else:
        # print("config not found")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'path': default_directory}
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        save_path = default_directory
        
    download_report(save_path, find_todays_filename())



if __name__ == '__main__':
    main()

