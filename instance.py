import csv
import numpy as np
import pandas as pd

data_size = 1000 

def gen_id(num):
    num = str(num)
    while len(num) < len(str(data_size)):
        num = '0' + num
    return num
def gen_id_prod(num):
    num = str(num)
    if len(num) < 2:
        num = '0' + num
    return num

def gen_date_of_start(since, term):
    day_since=int(since[0:2])
    if term[0:2]=='--':
        day_term=31
    else:
        day_term=int(term[0:2])
    month_since=int(since[3:5])
    if term[3:5]=='--':
        month_term=12
    else:
        month_term=int(term[3:5])
    year_since=int(since[6:10])
    if term[6:10]=='----':
        year_term=2023
    else:
        year_term=int(term[6:10])
    if year_term<2022:
        year = np.random.randint(year_since, year_term+1)
    else:
        year = np.random.randint(year_since, 2023)
    if year==year_term:
        month=np.random.randint(1, month_term+1)
        if month==month_term:
            day=np.random.randint(1, day_term+1)
        elif month in [4, 6, 9, 11]:
            day=np.random.randint(1, 31)
        elif month == 2:
            day=np.random.randint(1, 29)
        else:
            day=np.random.randint(1, 32)
    else:
        month=np.random.randint(1, 13)
        if month == 2:
            if year%4!=0:
                day = np.random.randint(1, 29)
            else:
                day = np.random.randint(1, 30)
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

def gen_date_of_term(since, term):
    day_since=int(since[0:2])
    if term[0:2]=='--':
        day_term=31
    else:
        day_term=int(term[0:2])
    month_since=int(since[3:5])
    if term[3:5]=='--':
        month_term=12
    else:
        month_term=int(term[3:5])
    year_since=int(since[6:10])
    if term[6:10]=='----':
        year_term=2023
    else:
        year_term=int(term[6:10])
    if year_since+4<year_term:
        year = np.random.randint(year_since, year_since+5)
    else:
        year = np.random.randint(year_since, year_term+1)
    if year==year_term:
        month=np.random.randint(1, month_term+1)
        if month==month_term:
            day=np.random.randint(1, day_term+1)
        elif month in [4, 6, 9, 11]:
            day=np.random.randint(1, 31)
        elif month == 2:
            day=np.random.randint(1, 29)
        else:
            day=np.random.randint(1, 32)
    else:
        month=np.random.randint(1, 13)
        if month == 2:
            if year%4!=0:
                day = np.random.randint(1, 29)
            else:
                day = np.random.randint(1, 30)
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

def gen_status(date_of_term):
    month=int(date_of_term[3:5])
    year=int(date_of_term[6:10])
    if year>2022 or (month>2 and year==2022):
        return "active"
    else:
        return "inactive"

def gen_distribution():
    gen=np.random.randint(1,10)
    if gen > 6:
        return "phyzical"
    else:
        return "web"

def gen_termination(status):
    if status=="inactive":
        return term_day
    else:
        return "----------"

columns = ["id","id-customer", "id-product", "active-day","termination-day",
    "status", "distribution"]

reader=pd.read_csv("D:\\new\\customers_data.csv", delimiter=',', names = ["id","id-customer", "id-product", "active-day","termination-day",
    "status", "distribution"])

data = pd.read_csv("D:\\new\\customers_data.csv")
since=data['customer_since'].tolist()
term=data['termination_date'].tolist()
ids=[i for i in range(1,data_size + 1)]
writer = pd.DataFrame([columns], columns=columns)
writer.to_csv("D:\\new\\instance.csv",mode='w', index=False, header=False)
ID=0
for i in range(data_size):
    number=np.random.randint(0,data_size-i)
    id_customer=ids[number]
    start=since[number]
    termination=term[number]
    ids.pop(number)
    id_customer=gen_id(id_customer)
    for j in range(np.random.randint(1,3)):
        ID+=1
        id_product=np.random.randint(1,21)
        active_day=gen_date_of_start(start, termination)
        term_day=gen_date_of_term(active_day, termination)
        status=gen_status(term_day)
        distribution=gen_distribution()
        if id_product in [2, 6, 7, 11, 12, 13, 15, 20]:
            if id_product == 2:
                writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(1), active_day, gen_termination(status), status, distribution]], columns=columns)
                writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
            elif id_product == 6 or id_product == 7:
                writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(5), active_day, gen_termination(status), status, distribution]], columns=columns)
                writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
            elif id_product >10 and id_product < 14:
                writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(10), active_day, gen_termination(status), status, distribution]], columns=columns)
                writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
            elif id_product == 15:
                writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(14), active_day, gen_termination(status), status, distribution]], columns=columns)
                writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
            else:
                writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(19), active_day, gen_termination(status), status, distribution]], columns=columns)
                writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
            ID+=1
            active_day=gen_date_of_start(active_day, term_day)
            term_day=gen_date_of_term(active_day, term_day)
            status=gen_status(term_day)
            distribution=gen_distribution()
        writer = pd.DataFrame([[gen_id(ID), id_customer, gen_id_prod(id_product), active_day, gen_termination(status), status, distribution]], columns=columns)
        writer.to_csv('D:\\new\\instance.csv', mode='a', index=False, header=False)
    term.pop(number)
    since.pop(number)
