from datetime import datetime
import requests
from bs4 import BeautifulSoup


# get by date
def get_prayer_times(currentMonth, *currentDay):
    """Return the time of prayer for today"""
    url = f'https://islom.uz/vaqtlar/14/{currentMonth}'

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    block = soup.find('tbody')

    try:
        for data in currentDay:
            day = block.find_all('td')[(data-1)*9+1].text
            prayer_day = block.find_all('td')[(data-1)*9+2].text
            Fajr = block.find_all('td')[(data-1)*9+3].text
            Sunrise = block.find_all('td')[(data-1)*9+4].text
            Dhuhr = block.find_all('td')[(data-1)*9+5].text
            Asr = block.find_all('td')[(data-1)*9+6].text
            Maghrib = block.find_all('td')[(data-1)*9+7].text
            Isha = block.find_all('td')[(data-1)*9+8].text

            return f'{day} {prayer_day}\nТонг(Саҳарлик) : {Fajr}\nҚуёш : {Sunrise}\nПешин : {Dhuhr}\nАср : {Asr}\nШом(Ифтор) : {Maghrib}\nХуфтон : {Isha}\n'
    except IndexError:
        print('Маълумот топилмади!')



def get_prayer_times_for_today():
    today = datetime.now().day
    currentMonth= datetime.now().month
    return get_prayer_times(currentMonth, today)
        

def get_prayer_times_for_tomorrow():
    today = datetime.now().day
    currentMonth= datetime.now().month
    return get_prayer_times(currentMonth, today+1)

def get_prayer_times_for_three_days():
    today = datetime.now().day
    currentMonth= datetime.now().month
    print( get_prayer_times(currentMonth, today+1, today+2, today+3))

def get_prayer_times_for_week():
    today = datetime.now().day
    currentMonth= datetime.now().month
    return get_prayer_times(currentMonth, today+1, today+2, today+3, today+4, today+5, today+6, today+7)


if __name__ == '__main__':
    get_prayer_times_for_three_days()