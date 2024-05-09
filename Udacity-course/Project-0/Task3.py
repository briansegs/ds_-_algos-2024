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


fixed = set()
mobile = set()
tele = set()

fixed_count = 0
call_count = 0

for call in calls: # -------- 0(n)
    out_call = call[0]
    in_call = call[1]

    if out_call.startswith('(080)'): # -------- 0(n)?
        call_count += 1

        if in_call.startswith('(0'): # -------- 0(n)?
            fixed.add(in_call[1:4])
            if in_call[:5] == '(080)':
                fixed_count += 1

        elif in_call[5] == " " and in_call.startswith(('7', '8', '9')): # -------- 0(n)?
            mobile.add(in_call[:4])

        elif in_call.startswith('140'): # -------- 0(n)?
            tele.add(in_call)

# Part A

bang_codes = sorted(list(fixed.union(mobile, tele))) # -------- 0(n log n)

print("The numbers called by people in Bangalore have codes:")
for code in bang_codes:
    print(code)

# Part B

percentage = round(100 * float(fixed_count)/float(call_count), 2)

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# runtime is 0(n log n) or 0(n^2)
