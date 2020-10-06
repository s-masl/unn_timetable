import datetime

Today = datetime.date.today()
Yesterday = Today + datetime.timedelta(days = 1)

today = Today.strftime("%Y.%m.%d")
tommorow = Yesterday.strftime("%Y.%m.%d")
