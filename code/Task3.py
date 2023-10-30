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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART A
bangalore_codes = list()
mobile_codes = list()
total_list = list()
bangalore_bangalore = list()

for call in calls:
    caller = call[0]
    if not caller.startswith('(080)'):
        continue
    receiver = call[1]
    total_list.append(receiver)
    if receiver.startswith('('): # all area codes
        stop = receiver.find(')')+1
        area_code = receiver[:stop]
        bangalore_codes.append(area_code)
    if receiver.startswith('(080)'): # bangalore to bangalore
        bangalore_bangalore.append(receiver)
    if receiver.startswith(('7', '8', '9')): # cell phones
        area_code = receiver[:4]
        mobile_codes.append(area_code)

# PART B 
pcnt = round(100*len(bangalore_bangalore)/len(total_list), 2)


# PRESENT RESULTS
print("The numbers called by people in Bangalore have codes:\n")
[print(num) for num in sorted(set(bangalore_codes))]
print()
[print(num) for num in sorted(set(mobile_codes))]
print()
print(f"{pcnt} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
