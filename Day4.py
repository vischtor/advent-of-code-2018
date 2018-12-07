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


input = open("Day4.txt", "r")
data = [val for val in input.read().replace("+","").split('\n') if val]

events = [Event(event) for event in data]

guards_total_sleep_time = defaultdict(int)
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
            guards_total_sleep_time[event.guard_id] += minute_diff
            for minute in range(sleep_time.minute,event.time_stamp.minute):
                if event.guard_id not in guards_minute_sleep_time:
                    guards_minute_sleep_time[guard_id] = defaultdict(int)
                guards_minute_sleep_time[guard_id][minute] += 1

most_sleeping_guard = max(guards_total_sleep_time.items(), key=lambda guard: guard[1])
most_asleep_minute = max(guards_minute_sleep_time[most_sleeping_guard[0]].items(), key=lambda minute: minute[1])

print(most_sleeping_guard[0] * most_asleep_minute[0])
