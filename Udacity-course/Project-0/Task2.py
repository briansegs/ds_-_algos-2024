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

num_dur = {}
caller = ''
num = 0

for call in calls:
    num1 = call[0]
    num2 = call[1]
    dur = int(call[3])

    if num1 not in num_dur:
        num_dur[num1] = dur

    elif num2 not in num_dur:
        num_dur[num2] = dur

    elif num1 in num_dur:
        num_dur[num1] += dur
        if num_dur[num1] > num:
            caller = num1
            num = num_dur[num1]

    elif num2 in num_dur:
        num_dur[num2] += dur
        if num_dur[num2] > num:
            caller = num2
            num = num_dur[num2]


print(f'{caller} spent the longest time, {num} seconds, on the phone during September 2016.')

# runtime is 0(n)
