#!/usr/bin/python3
"""
Module that scrapes hodor level_1 voting site for the
hidden key
"""
import requests
import bs4


def scrape_vote_num():
    """
    A function that will scrape the number of votes
    a sure already has
    """

    s = requests.Session()
    res = s.get('http://158.69.76.135/level4.php')
    # create beautiful soup object from response
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    s.close()
    table_list = []
    table = soup.find_all('table')[0]
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        for column in columns:
            table_list.append(column.get_text().strip())

    id_index = (table_list.index('675'))


    print(int(table_list[id_index + 1]))
    return(int(table_list[id_index + 1]))

if __name__ == '__main__':
    scrape_vote_num()
