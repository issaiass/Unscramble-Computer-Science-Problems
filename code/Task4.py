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

phone0 = list(set([call[0] for call in calls])) # outgoing call
phone1 = list(set([call[1] for call in calls])) # receive call
phone2 = list(set([call[0] for call in texts])) # send text
phone3 = list(set([call[1] for call in texts])) # receive text



telemarketer_numbers = list()
telemarketer_code = dict()
for call in calls:
    outgoing_call = call[0]
    if not outgoing_call.startswith('140'): # lookup another if not telemarketing
        continue
    if outgoing_call in phone2: # lookup another if send text
        continue
    if outgoing_call in phone3: # lookup another if receive text
        continue
    if outgoing_call in phone1: # lookup another if receive incoming calls
        continue
    telemarketer_numbers.append(outgoing_call) # append if fullfill requirements

telemarketer_numbers = list(set(sorted(telemarketer_numbers)))

print("These numbers could be telemarketers: ")
[print(num) for num in telemarketer_numbers]