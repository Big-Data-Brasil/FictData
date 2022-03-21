import numpy as np
import pandas as pd
import datetime
import csv

data_size = 1000


def gen_roaming():
    gen = np.random.randint(1, 10)
    if gen < 9:
        return "----------"
    else:
        return "roaming"


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = np.random.randint(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return np.random.randint(range_start, range_end)


def gen_phone():
    country_code = np.random.randint(1, 1000)
    area_code = np.random.randint(11, 100)
    phone_str = "+" + str(country_code) + "-" + str(area_code) + "-" + str(random_with_N_digits(8))
    return phone_str


customer = pd.read_csv('customers_data.csv')

columns = ["event_id", "product_id", "date", "total_volume", "event_type", "direction", "roaming", "calling_msisdn", "called_msisdn"]
ids = [i for i in range(1, data_size + 1)]

with open("costed_event.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\r')
    writer.writerow(columns)

ID = 0
for i in range(data_size):
    with open('costed_event.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\r')

        number = np.random.randint(0, data_size - i)
        id_product = ids[number]

        for j in range(np.random.randint(1, 10)):
            ID += 1

            start_date = datetime.datetime(2022, 3, 1, 0, 0, 0)
            term_date = datetime.datetime(2022, 3, 8, 0, 0, 0)
            date = random_date(start_date, term_date)

            event_type = np.random.choice(['call', 'sms', 'data'])
            if event_type == 'call':
                total_volume = np.random.randint(1, 50)
            if event_type == 'sms':
                total_volume = 1
            if event_type == 'data':
                total_volume = np.random.randint(1, 200)

            roaming = gen_roaming()

            direction = np.random.choice(['outgoing', 'incoming'])

            gen = np.random.randint(1, 15)
            if direction == 'outgoing':
                customer_id = np.random.choice(customer.MSISDN)
                if gen < 14:
                    customer2_id = np.random.choice(customer.MSISDN)
                else:
                    customer2_id = gen_phone()

            if direction == 'incoming':
                if gen < 14:
                    customer_id = np.random.choice(customer.MSISDN)
                else:
                    customer_id = gen_phone()
                customer2_id = np.random.choice(customer.MSISDN)

            if (customer_id != customer2_id):
                writer.writerow(
                    [ID, id_product, date, total_volume, event_type, direction, roaming, customer_id, customer2_id])
