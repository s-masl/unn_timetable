import requests
import shelve


def timeTable(date, group_id):
    link = 'https://portal.unn.ru/auth/index.php?login=yes&backurl=%2Fruz%2Fmain'
    timeTableLink = f'https://portal.unn.ru/ruzapi/schedule/group/{group_id}?start={date}&finish={date}&lng=1'

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


def make_user(user_id, group_id):
    with shelve.open(r'shelve\users') as users:
        users[f"{user_id}"] = group_id


def read_user(user_id):
    with shelve.open(r'shelve\users') as users:
        return users[user_id]


def groupID_to_name(groupid):
    return {
        28659: '382003-0',
        28655: '382003-1',
        28656: '382003-2',
        28657: '382003-3',
        28658: '382003-4',
        29799: '382003-1м',
        29794: '382003-2м',
        29798: '382003-3м',
        29800: '382003-4м',
        28713: '382003-в1',
        28714: '382003-в2',
    }[groupid]

