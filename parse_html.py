# This module parses sites with BeautifulSoup

from bs4 import BeautifulSoup


def parse_search_results(html: str) -> list:
    """Get search results to a list of dictionaries if more than one band
    return list of dictionaries"""

    results = []
    count = 0
    soup = BeautifulSoup(html, 'lxml')

    search_results = soup.find('tbody')
    if 'dataTables_empty' in str(search_results):
        return
    for table_row in search_results.find_all('tr'):
        table_data = table_row.find_all('td')
        count += 1
        result_dict = {'num': count, 'name': table_data[0].text, 'href': table_data[0].find('a', href=True)['href'],
                       'genre': table_data[1].text, 'country': table_data[2].text}
        results.append(result_dict)

    return results


def parse_main_info(html: str) -> dict:
    """This function gets all the basic info from the html"""

    basic_info = {}
    print("Getting basic info about the band.")
    soup = BeautifulSoup(html, 'lxml')

    # get header
    basic_info['name'] = soup.find('h1', class_='band_name').text

    # get basic info from left and right column
    left = soup.find('dl', class_='float_left')
    info = left.find_all(['dd', 'dt'])
    right = soup.find('dl', class_='float_right')
    info_right = right.find_all(['dd', 'dt'])
    for element in info_right:
        info.append(element)

    # TODO: add info from columns to basic info dictionary in a loop

    # TODO: get general comment for the band

    return basic_info


def parse_band_page(html: str):
    """This is the main point for the parsing of the band's page"""

    main_info = parse_main_info(html)
    print(main_info)

# this part below for testing offline
# with open('test_data/search_results.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_search_results(html_string)
# with open('test_data/band_site.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_band_page(html_string)
