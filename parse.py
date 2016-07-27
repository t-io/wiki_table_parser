import csv
import requests
from bs4 import BeautifulSoup


def main():
    print 'Parse Site'
    data = []
    url = ('https://de.wikipedia.org/wiki/Liste_der_deutschen_'
           'Landkreise_und_St%C3%A4dte_mit_ihren_Kfz-Kennzeichen')
    raw_site = get_raw_site_data(url)
    if raw_site:
        table_data = raw_site.body.find_all('table', class_='wikitable sortable')
        table = table_data[1]  # get the second matching table from the site

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if cells:
                try:
                    data.append([cells[0].get_text(), cells[4].get_text(), cells[5].get_text()])
                except:   # something went wrong, can't get expected data
                    pass  # ignore it

    print 'Write CSV'
    writeCSV(data)


def writeCSV(data_list):
    with open('data2.csv', 'wb') as data_file:
        csv_writer = csv.writer(data_file)
        for data in data_list:
            csv_writer.writerow([s.encode('utf-8') for s in data])  # write csv values in unicode


def get_raw_site_data(url):
    html = requests.get(url)
    return BeautifulSoup(html.text, 'lxml') if html.text else None


if __name__ == "__main__":
    main()
