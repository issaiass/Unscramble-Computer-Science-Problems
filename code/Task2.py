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



phone0 = [call[0].replace(' ', '_') for call in calls]
phone1 = [call[1].replace(' ', '_') for call in calls]
phones = list()
phones.extend(phone0)
phones.extend(phone1)
time = dict(zip(phones, len(phones)*[0]))

for call in calls:
    t = int(call[3])
    time[call[0].replace(' ', '_')] += t
    time[call[1].replace(' ', '_')] += t

max_time = max(time.values())
max_phone = dict(zip(time.values(), time.keys()))
print(f'{max_phone[max_time]} spent the longest time, {max_time} seconds, on the phone during September 2016') 