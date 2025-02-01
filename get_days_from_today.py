from datetime import datetime

def get_days_from_today(when_this_day:str):  #вхідні дані - дата у форматі:"string"
    #try:                                #на випадок отримання даних у не правильному форматі
        today = datetime.today().date()    #поточна дата у форматі datetime
        # today_date = today.strftime("%Y-%m-%d") # перетворення поточної дати у рядок
        # t=datetime.strptime(today_date,"%Y-%m-%d")  # перетворення поточної дати у об'єкт datetime без вказання годин, секунд і т.д
        now_date = datetime.strptime(when_this_day,"%Y-%m-%d").date()  #перетворення вхідної дати у об'єкт datatime
        delta_days = (now_date - today).days   #різниця між вхідною і поточною датами у ДНЯХ
        return delta_days #повернення результату ф-ії
    #except:
       #return  "неправильний формат даних"  #повідомлення про неправильний формат 

print(get_days_from_today("2025-02-28"))
