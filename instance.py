import numpy as np
import pandas as pd
import datetime as dt

data_size = 10000


def gen_date_of_start(since, term):
    since = dt.date.fromisoformat(since)
    day_since=since.day
    month_since = since.month
    year_since = since.year
    if term == "----------":
        day_term=31
        month_term = 12
        year_term = 2023
    else:
        term = dt.date.fromisoformat(term)
        day_term=term.day
        month_term=term.month
        year_term=term.year
    if year_term<2022:
        year = np.random.randint(year_since, year_term+1)
    else:
        year = np.random.randint(year_since, 2023)
    if year==year_term:
        if year==year_since:
            month=np.random.randint(month_since, month_term+1)
            if month==month_term:
                if month==month_since:
                    day=np.random.randint(day_since, day_term+1)
                else:
                    day=np.random.randint(1, day_term+1)
            elif month in [4, 6, 9, 11]:
                day=np.random.randint(1, 31)
            elif month == 2:
                day=np.random.randint(1, 29)
            else:
                day=np.random.randint(1, 32)
        else:
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
        if year==year_since:
            month=np.random.randint(month_since, 13)
            if month==month_since:
                if month == 2:
                    if year%4!=0:
                        day = np.random.randint(day_since, 29)
                    else:
                        day = np.random.randint(day_since, 30)
                elif month in [4, 6, 9, 11]:
                    day = np.random.randint(day_since, 31)
                else:
                    day = np.random.randint(day_since, 32)
            else:
                day=np.random.randint(1, 29)
        else:
            month=np.random.randint(1, month_term+1)
            if month == 2:
                if year%4!=0:
                    day = np.random.randint(1, 29)
                else:
                    day = np.random.randint(1, 30)
            elif month in [4, 6, 9, 11]:
                day = np.random.randint(1, 31)
            else:
                day = np.random.randint(1, 32)
    return dt.date(year=year, month=month, day=day).isoformat()

def gen_date_of_term(since, term):
    since = dt.date.fromisoformat(since)
    day_since = since.day
    month_since = since.month
    year_since = since.year
    if term == "----------":
        day_term=31
        month_term = 12
        year_term = 2023
    else:
        term = dt.date.fromisoformat(term)
        day_term=term.day
        month_term=term.month
        year_term=term.year
    if year_since+4<year_term:
        year = np.random.randint(year_since, year_since+5)
    else:
        year = np.random.randint(year_since, year_term+1)
    if year==year_term:
        if year==year_since:
            month=np.random.randint(month_since, month_term+1)
            if month==month_term:
                if month==month_since:
                    day=np.random.randint(day_since, day_term+1)
                else:
                    day=np.random.randint(1, day_term+1)
            elif month==month_since:
                if month in [4, 6, 9, 11]:
                    day=np.random.randint(day_since, 31)
                elif month == 2:
                    day=np.random.randint(day_since, 29)
                else:
                    day=np.random.randint(day_since, 32)
            elif month in [4, 6, 9, 11]:
                day=np.random.randint(1, 31)
            elif month == 2:
                day=np.random.randint(1, 29)
            else:
                day=np.random.randint(1, 32)
        else:
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
        if year==year_since:
            month=np.random.randint(month_since, 13)
            if month==month_since:
                if month == 2:
                    if year%4!=0:
                        day = np.random.randint(day_since, 29)
                    else:
                        day = np.random.randint(day_since, 30)
                elif month in [4, 6, 9, 11]:
                    day = np.random.randint(day_since, 31)
                else:
                    day = np.random.randint(day_since, 32)
            else:
                day=np.random.randint(1, 29)
        else:
            month=np.random.randint(1, 13)
            if month in [4, 6, 9, 11]:
                day=np.random.randint(1, 31)
            elif month == 2:
                day=np.random.randint(1, 29)
            else:
                day=np.random.randint(1, 32)
            if month == 2:
                if year%4!=0:
                    day = np.random.randint(1, 29)
                else:
                    day = np.random.randint(1, 30)
            elif month in [4, 6, 9, 11]:
                day = np.random.randint(1, 31)
            else:
                day = np.random.randint(1, 32)
    return dt.date(year=year, month=month, day=day).isoformat()

def gen_status(date_of_term):
    date_of_term = dt.date.fromisoformat(date_of_term)
    month = date_of_term.month
    year = date_of_term.year
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

columns = ["id","customer_id", "product_id", "activation_date","termination_date",
    "status", "distribution"]

customer=pd.read_csv("customer.csv")

since=customer['customer_since'].tolist()
term=customer['termination_date'].tolist()
ids=[i for i in range(1,data_size + 1)]
instance = pd.DataFrame([columns], columns=columns)
instance.to_csv("instance.csv",mode='w', index=False, header=False)
ID=0
for i in range(data_size):
    number=np.random.randint(data_size-i)
    id_customer=ids.pop(number)
    start=str(since[number])
    termination=str(term[number])
    for j in range(np.random.randint(1,3)):
        ID+=1
        id_product=np.random.randint(1,21)
        active_day=gen_date_of_start(start, termination)
        term_day=gen_date_of_term(active_day, termination)
        status=gen_status(term_day)
        distribution=gen_distribution()
        if id_product in [2, 6, 7, 11, 12, 13, 15, 20]:
            if id_product == 2:
                writer = pd.DataFrame([[ID, id_customer, 1, active_day, gen_termination(status), status, distribution]])
                writer.to_csv('instance.csv', mode='a', index=False, header=False)
            elif id_product == 6 or id_product == 7:
                writer = pd.DataFrame([[ID, id_customer, 5, active_day, gen_termination(status), status, distribution]])
                writer.to_csv('instance.csv', mode='a', index=False, header=False)
            elif id_product >10 and id_product < 14:
                writer = pd.DataFrame([[ID, id_customer, 10, active_day, gen_termination(status), status, distribution]])
                writer.to_csv('instance.csv', mode='a', index=False, header=False)
            elif id_product == 15:
                writer = pd.DataFrame([[ID, id_customer, 14, active_day, gen_termination(status), status, distribution]])
                writer.to_csv('instance.csv', mode='a', index=False, header=False)
            else:
                writer = pd.DataFrame([[ID, id_customer, 19, active_day, gen_termination(status), status, distribution]])
                writer.to_csv('instance.csv', mode='a', index=False, header=False)
            ID+=1
            active_day= gen_date_of_start(active_day, term_day)
            term_day=gen_date_of_term(active_day, term_day)
            status=gen_status(term_day)
            distribution=gen_distribution()
        writer = pd.DataFrame([[ID, id_customer, id_product, active_day, gen_termination(status), status, distribution]])
        writer.to_csv('instance.csv', mode='a', index=False, header=False)
    term.pop(number)
    since.pop(number)
