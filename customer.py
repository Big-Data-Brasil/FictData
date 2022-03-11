import numpy as np
import pandas as pd
import csv

data_size = 10000                      # задание объема данных


def gen_id(num):
    num = str(num)
    while len(num) < len(str(data_size)):
        num = '0' + num
    return num


def gen_first_name(gender):
    male_names = ['Jose', 'Joao', 'Antonio', 'Francisco', 'Carlos', 'Paulo',
                  'Pedro', 'Lucas', 'Luiz', 'Marcos']
    female_names = ['Maria', 'Ana', 'Franciska', 'Antonia', 'Andriana', 'Juliana',
                    'Marcia', 'Fernanda', 'Patricia', 'Aline']
    if gender == 'male':
        return np.random.choice(male_names)
    else:
        return np.random.choice(female_names)


def gen_last_name():
    last_names = ['Silva', 'Santos', 'Sousa', 'Oliveira', 'Pereira', 'Lima', 'Carvalho',
                  'Ferreira', 'Rodrigues', 'Almeida', 'Costa', 'Gomes', 'Martins',
                  'Araujo', 'Melo', 'Barbosa', 'Alves', 'Ribeiro', 'Cardoso']
    return np.random.choice(last_names)


def gen_date_of_birth():
    month = np.random.randint(1, 13)
    if month == 2:
        day = np.random.randint(1, 29)
    elif month in [4, 6, 9, 11]:
        day = np.random.randint(1, 31)
    else:
        day = np.random.randint(1, 32)
    day = str(day)
    if len(day) == 1:
        day = '0' + day
    month = str(month)
    if len(month) == 1:
        month = '0' + month
    first_part = np.random.normal(loc=20, scale=5, size=100)
    second_part = np.random.normal(loc=36, scale=20, size=1000)
    third_part = np.random.normal(loc=55, scale=20, size=300)
    age_distribution = np.concatenate([first_part, second_part, third_part])
    age_distribution = age_distribution[(age_distribution < 100) & (age_distribution >= 19)]
    year = 2022 - int(np.random.choice(age_distribution))
    return day + '-' + month + '-' + str(year)

def gen_date_of_start(date_of_birth):
    year=int(date_of_birth[6:10])
    if year<=1977:
        year = np.random.randint(1995, 2023)
    else:
        year = np.random.randint(year+18, 2023)
    if year<2022:
        month=np.random.randint(1, 13)
        if month == 2:
            if year%4==0:
                day = np.random.randint(1, 30)
            else:
                day = np.random.randint(1, 29)
        elif month in [4, 6, 9, 11]:
            day = np.random.randint(1, 31)
        else:
            day = np.random.randint(1, 32)
    else:
        month=np.random.randint(1, 3)
        if month == 2:
            day = np.random.randint(1, 29)
        else:
            day = np.random.randint(1, 32)
    day = str(day)
    if len(day) == 1:
        day = '0' + day
    month = str(month)
    if len(month) == 1:
        month = '0' + month
    return day + '-' + month + '-' + str(year)

def gen_date_of_term(date_of_start):
    month=np.random.randint(1, 13)
    year=int(date_of_start[6:10])
    year = np.random.randint(year+1, 2060)
    month=np.random.randint(1, 13)
    if month == 2:
        day = np.random.randint(1, 29)
    elif month in [4, 6, 9, 11]:
        day = np.random.randint(1, 31)
    else:
        day = np.random.randint(1, 32)
    day = str(day)
    if len(day) == 1:
        day = '0' + day
    month = str(month)
    if len(month) == 1:
        month = '0' + month
    return day + '-' + month + '-' + str(year)

def gen_promo_agreement(date_of_birth):
    age = 2022 - int(date_of_birth[-4:])
    if age < 25:
        return np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
    elif age < 30:
        return np.random.choice(['Yes', 'No'], p=[0.4, 0.6])
    elif age < 40:
        return np.random.choice(['Yes', 'No'], p=[0.2, 0.8])
    elif age < 50:
        return np.random.choice(['Yes', 'No'], p=[0.05, 0.95])
    else:
        return 'No'

def gen_card():
    card=np.random.randint(0,9, size=16)
    card_str=""
    chance=np.random.randint(0,10)
    if chance<8:
        for i in range(16):
            card_str+=str(card[i])
    else:
        card_str="----------"
    return card_str

def gen_phone():
    phone=np.random.randint(0,9, size=10)
    phone_str="+55-"
    phone_str+=str(phone[0])+str(phone[1])+"-"
    for i in range(8):
        phone_str+=str(phone[i])
    return phone_str

def gen_status(date_of_term):
    month=int(date_of_term[3:5])
    year=int(date_of_term[6:10])
    if year>2022 or (month>2 and year==2022):
        return "active"
    else:
        return "inactive"
    
def gen_category():
    gen=np.random.randint(1,10)
    if gen < 8:
        return "phyzical"
    else:
        return "business"

def gen_region():
    gen=np.random.randint(1,15)
    if gen>9:
        return "San_Paulo"
    elif gen>5:
        return "Rio-de-Zhaneiro"
    elif gen>3:
        return "Salvador"
    elif gen>1:
        return "Brasilia"
    else:
        return "Fortalesa"

def gen_language():
    gen=np.random.randint(1,10)
    if gen>3:
        return "portuguese"
    elif gen>1:
        return "english"
    else:
        return "russian"

def gen_termination(status):
    if status=="inactive":
        return termination_date
    else:
        return "----------"

columns = ['Customer_ID', 'First name', 'Last name', 'date of birth',        # колонки в таблице
           'gender', 'agree_for_promo', 'autopay_card', 'email', 'MSISDN',
           'Status', 'customer category', 'customer_since', 'region',
           'language', 'termination_date']


#with open("D:\\new\\customers_data.csv", "w") as file:           # создание csv файла с заданными колонками
    #writer = csv.writer(file, lineterminator='\r')
    #writer.writerow(columns)
writer = pd.DataFrame([columns], columns=columns)
writer.to_csv("D:\\new\\customers_data.csv",mode='w', index=False, header=False)            # заполнение таблицы данными
for i in range(data_size):
    ID = gen_id(i + 1)
    gender = np.random.choice(['male', 'female'])
    f_name = gen_first_name(gender)
    l_name = gen_last_name()
    date_of_birth = gen_date_of_birth()
    agree_for_promo = gen_promo_agreement(date_of_birth)
    card = gen_card()
    email = f_name.lower()[0:4] + '.' + l_name.lower()[0:5] + date_of_birth[-2:] + '@gmail.com'
    msisdn = gen_phone()
    category = gen_category()
    since = gen_date_of_start(date_of_birth)
    region = gen_region()
    language = gen_language()
    termination_date = gen_date_of_term(since)
    status = gen_status(termination_date)
    termination_date = gen_termination(status)
    writer = pd.DataFrame([[ID, f_name, l_name, date_of_birth, gender, agree_for_promo, card, email, msisdn, status, category, since, region, language, termination_date]], columns=columns)
    writer.to_csv('D:\\new\\customers_data.csv', mode='a', index=False, header=False)
