import datetime


def today():
    return datetime.date.today().strftime("%Y.%m.%d")


def tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y.%m.%d")
