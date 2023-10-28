"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def call_buffer(data, phone_numbers_buffer):
    for text in data:
        sending_num = text[0]
        receiving_num = text[1]
        if sending_num not in phone_numbers_buffer:
            phone_numbers_buffer.append(sending_num)
        if receiving_num not in phone_numbers:
            phone_numbers_buffer.append(receiving_num)
    return phone_numbers_buffer

phone_numbers = []
phone_numbers = call_buffer(texts, phone_numbers)
phone_numbers = call_buffer(calls, phone_numbers)


print(f"There are {len(phone_numbers)} different telephone numbers in the records.")