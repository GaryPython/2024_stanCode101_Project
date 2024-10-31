"""
File: webcrawler.py
Name: Gary
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup



def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        rows = soup.find_all('tr')
        male_cnt = 0
        female_cnt = 0
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 5:
                male_number = cells[2].text.replace(",", "")
                female_number = cells[4].text.replace(",", "")
                male_cnt += int(male_number)
                female_cnt += int(female_number)
        print(f'Male Number:{male_cnt}')
        print(f'Female Number:{female_cnt}')




if __name__ == '__main__':
    main()
