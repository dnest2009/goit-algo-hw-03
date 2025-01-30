from datetime import datetime

def get_days_from_today(date:str):  #вхідні дані - дата у форматі:"string"
    try:                                #на випадок отримання даних у не правильному форматі
        today = datetime.today().day        #поточна дата у форматі ДЕНЬ
        now_date = datetime.strptime(date,"%Y-%m-%d").day   #перетворення вхідної дати у об'єкт datatime ДЕНЬ
        delta_days = now_date - today     #різниця між вхідною і поточною датами у ДНЯХ
        return delta_days   #повернення результату ф-ії
    except:
        return "неправильний формат даних"  #повідомлення про неправильний формат даних

print(get_days_from_today("2025-01-31"))
