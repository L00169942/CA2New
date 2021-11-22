"""
# ----------------------
# Created : 15-11-2021 23:48
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""

import requests
import re
from bs4 import BeautifulSoup

url = "http://192.168.85.128/"


def parse_data():
    try:
        print('Inside data parse function')
        response = requests.get(url)
        parse_to_html = BeautifulSoup(response.content, "html.parser")
        return parse_to_html

    except Exception as e:
        print(e)


def get_title(parsed_data):
    """Q2.a start: Find heading"""
    try:
        print('Inside function 1')
        page_title = parsed_data.find("title").text
        print('Page title: '+page_title)  # Q2.a print the title of the page
    except Exception as e:
        print(e)


def get_word_count(parsed_data):
    """Q2.b start : count of Apache2 present"""
    print('inside function 2')
    try:
        page_content = parsed_data.find("body").text
        search_key = 'apache2'
        if search_key in page_content:
            word_count = page_content.lower().count(search_key)
            # word_count = page_content.count(search_key)
            print("Number of 'Apache2' found :",word_count)
    except Exception as e:
        print(e)

def get_numbers(parsed_data):
    print('inside function 3')
    """Q3 start # To read numbers those found in the page using regular expression"""
    try:
        page_content = parsed_data.find("body").text
        contents = str(page_content)
        numbers_list = re.findall('[0-9]+', contents)

        print("Numbers found in the page", numbers_list)  # print numbers found in the page
        # Count of numbers found in the list
        count_number_list = len(set(numbers_list))
        print("Number of unique elements in the list: ", count_number_list)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parsed_data = parse_data()
    get_title(parsed_data)  # Q2.a print the title of the page
    get_word_count(parsed_data)  # Q2.b count of Apache2 present
    get_numbers(parsed_data)  # Q2.c To read numbers,  those found on the page using regular expression
