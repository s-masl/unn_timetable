import requests


def timeTable(date):
    link = 'https://portal.unn.ru/auth/index.php?login=yes&backurl=%2Fruz%2Fmain'
    timeTableLink = f'https://portal.unn.ru/ruzapi/schedule/group/28655?start={date}&finish={date}&lng=1'

    data = {
        'AUTH_FORM': 'Y',
        'TYPE': 'AUTH',
        'backurl': '/auth/index.php?backurl=%2Fruz%2Fmain',
        'USER_LOGIN': 's20380366',
        'USER_PASSWORD': 'aezakmi69'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    s = requests.session()
    response = s.post(link, data=data, headers=headers)
    ttResponse = s.get(timeTableLink, data=data)
    if len(ttResponse.json()) != 0:
        strlesson = u"\U0001F4C5" + ' ' * 17 + ttResponse.json()[0]['date'] + ' ' + ttResponse.json()[0][
            'dayOfWeekString'] + ' ' * 20 + '\n\n'
        for i in range(len(ttResponse.json())):
            l = [ttResponse.json()[i]['discipline'],
                 ttResponse.json()[i]['kindOfWork'],
                 ttResponse.json()[i]['beginLesson'],
                 ttResponse.json()[i]['endLesson'],
                 ttResponse.json()[i]['building'],
                 ttResponse.json()[i]['auditorium']]
            strlesson += l[0] + '\n' + l[1] + '\n' + l[2] + '-' + l[3] + '\n' + l[4] + ' ' + l[5] + '\n\n'
        return strlesson
    else:
        return 'В этот день нет пар или некорректный ввод.'


def getInfo(message):
    return f'{message.from_user.first_name}  {message.from_user.last_name}\n{message.from_user.username}\n'

