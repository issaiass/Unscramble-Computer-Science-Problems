"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_time = 0
max_phone = str()
for call in calls:
    time = float(call[3])
    phone = call[1]

    if time > max_time:
        max_time = time
        max_phone = call[1]

print(f"{max_phone} spent the longest time, {max_time} seconds, on the phone during September 2016.")