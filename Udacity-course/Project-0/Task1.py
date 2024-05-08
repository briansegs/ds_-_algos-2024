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

records = texts + calls

numbers = []
count = 0

for record in records:
    num1 = record[0]
    num2 = record[1]

    if num1 not in numbers:
        count += 1
        numbers.append(num1)
    if num2 not in numbers:
        count += 1
        numbers.append(num2)

print(f'There are {count} different telephone numbers in the records.')

# runtime is 0(n)
