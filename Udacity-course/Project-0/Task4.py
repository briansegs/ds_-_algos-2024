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

callers = []
not_lst = []

for call in calls:
    calling_num = call[0]
    receiving_num = call[1]

    if calling_num  not in callers:
        callers.append(calling_num )

    if receiving_num not in not_lst:
        not_lst.append(receiving_num)

for text in texts:
    texting_num = text[0]
    texted_num = text[1]

    if texting_num not in not_lst:
        not_lst.append(texting_num)

    if texted_num not in not_lst:
        not_lst.append(texted_num)


possible_tele_nums = []

for caller in callers:
    if caller not in not_lst:
        possible_tele_nums.append(caller)

list_of_numbers = sorted(possible_tele_nums)

print("These numbers could be telemarketers: ")
for num in list_of_numbers:
    print(num)

# runtime is 0(n^2)
