import bs4
import pandas as pd
import json
from urllib.request import Request, urlopen
import glob

def scraper(page):
    with open('htmls/' + str(page) + '.html', 'r') as html:
        html = html.read()
        bs = bs4.BeautifulSoup(html)
        companies = []
        columns = [
            'company',
            'description',
            'website',
            'region',
            'year-selected',
            'vertical',
            'sub-vertical',
            'entrepreneurs',
            'fund',
            'financing-round',
            'status',
            'year-invested'
        ]
        for company_i in range(len(bs.find_all(class_='company-details-inner'))):
            company = []
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('h2').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find(class_=['company-description', 'small-paragraph']).text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('span', class_='website').find('a')['href'].strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('span',class_='region').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('span',class_='year-selected').text.split(' ')[1].strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('span',class_='vertical').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find('span',class_='sub-vertical').text.strip())
            except:
                company.append('')
            entrepreneurs = []
            for entrepreneur_i in range(len(bs.find_all(class_='company-details-inner')[company_i].find_all('span', class_='entrepreneur'))):
                entrepreneur = {}
                try:
                    entrepreneur['name'] = bs.find_all(class_='company-details-inner')[company_i].find_all('span', class_='entrepreneur')[entrepreneur_i].text.strip()
                except:
                    entrepreneur['name'] = ''
                try:
                    entrepreneur['url'] = bs.find_all(class_='company-details-inner')[company_i].find_all('span', class_='entrepreneur')[entrepreneur_i].find('a').get('href', {}).strip()
                except:
                    entrepreneur['url'] = ''
                entrepreneurs.append(json.dumps(entrepreneur))
            company.append(entrepreneurs)
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find(class_='investment-info').find(class_='fund').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find(class_='investment-info').find(class_='financing-round').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find(class_='investment-info').find(class_='status').text.strip())
            except:
                company.append('')
            try:
                company.append(bs.find_all(class_='company-details-inner')[company_i].find(class_='year-invested').text.strip())
            except:
                company.append('')
            companies.append(company)
        pd.DataFrame(companies, columns=columns).to_csv('csvs/'+ str(page) + '.csv', index=False)

