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
total_time = 0

for call in calls:
    out_num = call[0]
    in_num = call[1]
    duration = int(call[3])

    if out_num in num_dur:
        num_dur[out_num] += duration
        if num_dur[out_num] > total_time:
            caller = out_num
            total_time = num_dur[out_num]

    else:
        num_dur[out_num] = duration

    if in_num in num_dur:
        num_dur[in_num] += duration
        if num_dur[in_num] > total_time:
            caller = in_num
            total_time = num_dur[in_num]

    else:
        num_dur[in_num] = duration



print(f'{caller} spent the longest time, {total_time} seconds, on the phone during September 2016.')

# runtime is 0(n^2)
