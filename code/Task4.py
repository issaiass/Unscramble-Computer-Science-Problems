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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketer = set()
sending_texts = set([num[0] for num in texts])
receiving_texts = set([num[1] for num in texts])
sending_calls = set([num[0] for num in calls])
receiving_calls = set([num[1] for num in calls])

for out_call in sending_calls: 
    if out_call in sending_texts: # if in sending text is not telemarketer
        continue
    if out_call in receiving_texts: # if in receive texts is not telemarketer
        continue
    if out_call in receiving_calls: # if in receive calls is not telemarketer
        continue
    telemarketer.add(out_call) # might be telemarketers

telemarketer = sorted(telemarketer)  # sort it

print("These numbers could be telemarketers: ")
[print(num) for num in telemarketer] # print it