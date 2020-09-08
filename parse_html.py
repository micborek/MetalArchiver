"""This module is for parsing different sub-pages with BeautifulSoup"""
# TODO: create a 'parser' class

from bs4 import BeautifulSoup


def parse_search_results(html: str) -> list:
    """Get search results to a list of dictionaries if more than one band
    return list of dictionaries"""

    results = []
    count = 0
    soup = BeautifulSoup(html, 'lxml')

    search_results = soup.find('tbody')
    if 'dataTables_empty' in str(search_results):
        return results
    for table_row in search_results.find_all('tr'):
        table_data = table_row.find_all('td')
        count += 1
        result_dict = {'num': count, 'name': table_data[0].text, 'href': table_data[0].find('a', href=True)['href'],
                       'genre': table_data[1].text, 'country': table_data[2].text}
        results.append(result_dict)

    return results


def parse_main_info(html: str) -> dict:
    """This function gets the basic info from the html - header and top columns"""

    print("Getting basic info about the band.")
    soup = BeautifulSoup(html, 'lxml')

    # get basic info from left and right column
    basic_info = parse_float_left_right(soup)

    # get header
    basic_info['Name'] = soup.find('h1', class_='band_name').text

    return basic_info


def parse_float_left_right(html: BeautifulSoup) -> dict:
    """This one is for parsing floating columns which occur for band and release sites"""

    data = {}
    left = html.find('dl', class_='float_left')
    info = left.find_all(['dd', 'dt'])
    right = html.find('dl', class_='float_right')
    info_right = right.find_all(['dd', 'dt'])
    for element in info_right:
        info.append(element)

    count = 0
    for element in info:
        if count == 0:
            key = element.text
            count += 1
        else:
            data[key] = element.text.replace('\n', '')
            count = 0

    return data


def get_releases_links(html: str) -> dict:
    """This function gets the links for releases' info from the band's page """

    links = {}
    print('Getting releases links.')
    soup = BeautifulSoup(html, 'lxml')
    discography_table = soup.find('table', class_='display discog')
    disco_links = discography_table.find_all('a')
    for link in disco_links:
        if 'reviews' not in str(link['href']):
            links[link.text] = link['href']

    return links


def parse_release_data(html: str) -> dict:
    """This function gets data from the release page"""

    soup = BeautifulSoup(html, 'lxml')
    release_data = parse_float_left_right(soup)

    # get header
    release_data['Name'] = soup.find('h1', class_='album_name').text

    return release_data


# this part below for testing offline

# with open('test_data/search_results.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_search_results(html_string)

# with open('test_data/band_site.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_main_info(html_string)

# with open('test_data/band_site.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# get_releases_links(html_string)

# with open('test_data/release_site.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_release_data(html_string)
