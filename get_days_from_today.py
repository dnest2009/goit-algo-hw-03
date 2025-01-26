from datetime import datetime

def get_days_from_today(date:str):  #вхідні дані - дата у форматі:"string"
    try:
        today = datetime.today()        #поточна дата
        now_date = datetime.strptime(date,"%Y-%m-%d")   #перетворення вхідної дати у об'єкт datatime
        delta_days = (now_date - today).days            #різниця між вхідною і поточною датами у днях
        return delta_days                               #повернення результату ф-ії
    except:
        return "неправильний формат даних"

day = "24-01-2009"
x = get_days_from_today(day)
print (x)