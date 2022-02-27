from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# get by date
def get_prayer_times(currentMonth, *currentDay):
    """Return the time of prayer for today"""
    url = f'https://islom.uz/vaqtlar/14/{currentMonth}'

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    body = soup.find('tbody')
    head = soup.find('thead')

    try:
        for data in currentDay:
            day = body.find_all('td')[(data-1)*9+1].text
            month = head.find_all('th')[1].text
            prayer_day = body.find_all('td')[(data-1)*9+2].text
            Fajr = body.find_all('td')[(data-1)*9+3].text
            Sunrise = body.find_all('td')[(data-1)*9+4].text
            Dhuhr = body.find_all('td')[(data-1)*9+5].text
            Asr = body.find_all('td')[(data-1)*9+6].text
            Maghrib = body.find_all('td')[(data-1)*9+7].text
            Isha = body.find_all('td')[(data-1)*9+8].text

            return f'{day} {month.title()} {prayer_day}\n*🌅Тонг(Саҳарлик) : {Fajr}*\nҚуёш : {Sunrise}\nПешин : {Dhuhr}\nАср : {Asr}\n*🌄Шом(Ифтор) : {Maghrib}*\nХуфтон : {Isha}\n'
    except:
        return 'Маълумот топилмади!'


def get_prayer_times_for_today():
    today = datetime.now().day
    currentMonth = datetime.now().month
    return get_prayer_times(currentMonth, today)


def get_prayer_times_for_tomorrow():
    try:
        today = datetime.now().day
        currentMonth = datetime.now().month
        if currentMonth == 2 and today == 28:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 3 and today == 31:
            return get_prayer_times(currentMonth+1, 1)
        elif currentMonth == 4 and today == 30:
            return get_prayer_times(currentMonth+1, 1)
        else:
            return get_prayer_times(currentMonth, today+1)
    except:
        return 'Маълумот топилмади!'


def get_prayer_times_for_three_days():
    try:
        today = datetime.now().day
        currentMonth = datetime.now().month
        """check if last day of month add 1 to current month and take from 1 days"""
        if currentMonth == 2 and today == 27:
            next_day = get_prayer_times(currentMonth, today+1)
            next_month = get_prayer_times(currentMonth+1, 1) + '\n'
            next_month += get_prayer_times(currentMonth+1, 2) + '\n'
            return next_day + '\n' + next_month + '\n'
        elif currentMonth == 2 and today == 28:
            next_day = get_prayer_times(currentMonth+1, 1) + '\n'
            next_day += get_prayer_times(currentMonth+1, 2) + '\n'
            next_day += get_prayer_times(currentMonth+1, 3)
            return next_day
        elif currentMonth == 3 and 1 <= today <= 28 :
            next_day = get_prayer_times(currentMonth, today+1)+ '\n'
            next_day += get_prayer_times(currentMonth, today+2)+ '\n'
            next_day += get_prayer_times(currentMonth, today+3)
        elif currentMonth == 3 and today == 29:
            next_day = get_prayer_times(currentMonth, today+1)
            next_day += get_prayer_times(currentMonth, today+2)+ '\n'
            next_month = get_prayer_times(currentMonth+1, 1)
            return next_day + '\n' + next_month
        elif currentMonth == 3 and today == 30:
            next_day = get_prayer_times(currentMonth, today+1)
            next_month = get_prayer_times(currentMonth+1, 1) + '\n'
            next_month += get_prayer_times(currentMonth+1, 2)
            return next_day + '\n' + next_month
        elif currentMonth == 3 and today == 31:
            next_day = get_prayer_times(currentMonth+1, 1)
            next_day += get_prayer_times(currentMonth+1, 2)
            next_day += get_prayer_times(currentMonth+1, 3)
            return next_day + '\n'
        elif currentMonth == 4 and 1 <= today <= 27:
            next_day = get_prayer_times(currentMonth, today+1)
            next_day += get_prayer_times(currentMonth, today+2)
            next_day += get_prayer_times(currentMonth, today+3)
            return next_day + '\n'
        elif currentMonth == 4 and today == 28:
            next_day = get_prayer_times(currentMonth, today+1)
            next_day += get_prayer_times(currentMonth, today+2) + '\n'
            next_month = get_prayer_times(currentMonth+1, 1)
            return next_day + '\n' + next_month
        elif currentMonth == 4 and today == 29:
            next_day = get_prayer_times(currentMonth, today+1)
            next_month = get_prayer_times(currentMonth+1, 1)+ '\n'
            next_month += get_prayer_times(currentMonth+1, 2)
            return next_day + '\n' + next_month
        elif currentMonth == 4 and today == 30:
            next_day = get_prayer_times(currentMonth+1, 1)
            next_day += get_prayer_times(currentMonth+1, 2)+ '\n'
            next_day += get_prayer_times(currentMonth+1, 3)
            return next_day
    except:
        return 'Маълумот топилмади!'


def get_prayer_times_for_week():
    try:
        today = datetime.now().day
        currentMonth = datetime.now().month
        return get_prayer_times(currentMonth, today+1, today+2, today+3, today+4, today+5, today+6, today+7)
    except:
        return 'Маълумот топилмади!'


# not completed
def regions(region_name='Навои'):
    regionNames = ['Андижон', 'Бекобод', 'Бишкек', 'Бухоро', 'Гулистон',
                   'Денов', 'Каракол', 'Марғилон', 'Навои', 'Наманган', 'Нукус',
                   'Самарқанд', 'Қўқон', 'Қарши', 'Қўқон', 'Тошкент']

    if region_name == 'Андижон':
        regionId = 1
    elif region_name == 'Бекобод':
        regionId = 2
    elif region_name == 'Бишкек':
        regionId = 3
    elif region_name == 'Бухоро':
        regionId = 4
    elif region_name == 'Гулистон':
        regionId = 5
    elif region_name == 'Денов':
        regionId = 6
    elif region_name == 'Каракол':
        regionId = 9
    elif region_name == 'Марғилон':
        regionId = 13
    elif region_name == 'Навои':
        regionId = 14
    elif region_name == 'Наманган':
        regionId = 15
    elif region_name == 'Нукус':
        regionId = 16
    elif region_name == 'Самарқанд':
        regionId = 18
    elif region_name == 'Қўқон':
        regionId = 21
    elif region_name == 'Қарши':
        regionId = 25
    elif region_name == 'Қўқон':
        regionId = 26
    elif region_name == 'Тошкент':
        regionId = 27
    else:
        error = 'Маълумот топилмади!'

    # return {'name': region_name, 'id': regionId, 'error': error}
    pass


today = datetime.now().day
currentMonth = datetime.now().month


if __name__ == '__main__':
    print(get_prayer_times_for_three_days())