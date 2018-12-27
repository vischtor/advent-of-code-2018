from collections import defaultdict
from datetime import datetime
from enum import Enum

class Event_type(Enum):
    BEGIN_SHIFT = 1
    SLEEP = 2
    WAKE = 3

class Event:
    def __init__(self, event):
        self.guard_id = -1
        self.time_stamp = datetime.strptime(event[1:17], "%Y-%m-%d %H:%M")
        if "shift" in event:
            self.event_type = Event_type.BEGIN_SHIFT
            self.guard_id = int(event.split()[3].replace("#",""))
        elif "sleep" in event:
            self.event_type = Event_type.SLEEP
        elif "wake" in event:
            self.event_type = Event_type.WAKE

            
sample_input = "[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up\n"
sample_data = [val for val in sample_input.replace("+","").split('\n') if val]

input = open("Day4.txt", "r")
data = [val for val in input.read().replace("+","").split('\n') if val]

events = [Event(event) for event in data]

guards_minute_sleep_time = {}


events.sort(key=lambda x: x.time_stamp)
for event in events:
    if event.event_type == Event_type.BEGIN_SHIFT:
        guard_id = event.guard_id
    else:
        event.guard_id = guard_id
        if event.event_type == Event_type.SLEEP:
            sleep_time = event.time_stamp
        elif event.event_type == Event_type.WAKE:
            diff = event.time_stamp - sleep_time
            minute_diff = int(diff.seconds / 60)
            for minute in range(sleep_time.minute,event.time_stamp.minute):
                if event.guard_id not in guards_minute_sleep_time:
                    guards_minute_sleep_time[guard_id] = defaultdict(int)
                guards_minute_sleep_time[guard_id][minute] += 1

favourite_minute = {}
for guard in guards_minute_sleep_time:
    favourite_minute[guard] = max(guards_minute_sleep_time[guard].items(), key=lambda g:g[1])

best = (max(favourite_minute.items(), key=lambda g:g[1][1]))
best_guard_id = best[0]
best_minute = best[1][0]
print(best_guard_id, best_minute)
print(best_guard_id * best_minute)




