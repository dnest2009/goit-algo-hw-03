import random #імпорт модуля рандомних чисел

def get_numbers_ticket(min, max, quantity): 
    get_numbers_ticket=[]  #створюємо пустий список
    i=int(0)  #присвоюємо лічильнику початкове значення
    try:      
        if max>min and min>=1 and max<=1000 and quantity<=max-min+1:   #перевірка вхідних параметрів 
            while i < quantity:          
                x = random.randint(min, max)      #рандомне число між min та max
                if x not in get_numbers_ticket:        #перевірка чи є вже дане число у списку
                    get_numbers_ticket.append(x)      #додати число у список
                    i=i+1                            #лічильник +1
            get_numbers_ticket.sort()                #сортування чисел у списку за зростанням
            return get_numbers_ticket             #результат список чисел
        else:
            return get_numbers_ticket              #результат пустий список, невірний формат вхідних параметрів
    except:
        return get_numbers_ticket              #результат пустий список, невірний формат вхідних параметрів

print(get_numbers_ticket(10,6,10))