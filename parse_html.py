# This module parses sites with BeautifulSoup

from bs4 import BeautifulSoup


def parse_search_results(html: str):
    """Get search results to a list of dictionaries if more than one band"""

    results = []
    count = 0
    soup = BeautifulSoup(html, 'lxml')

    search_results = soup.find('tbody')
    for table_row in search_results.find_all('tr'):
        table_data = table_row.find_all('td')
        count += 1
        result_dict = {'num': count, 'name': table_data[0].text, 'href': table_data[0].find('a', href=True)['href'],
                       'genre': table_data[1].text, 'country': table_data[2].text}
        results.append(result_dict)

    return results


# this part below for testing offline
# with open('test_data/search_results.html', 'r', encoding='utf8') as f:
#     html_string = f.read()
# parse_search_results(html_string)
