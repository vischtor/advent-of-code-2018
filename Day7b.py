def job_time(job):
    return (ord(job) - 64) + 60

input = open("Day7.txt", "r")
data = [val.split() for val in input.read().split('\n') if val]

right = {}
left = {}
all_nodes = set()

for instruction in data:
    parent = instruction[1]
    this = instruction[7]
    if this in left:
        left[this].append(parent)
    else:
        left[this] = [parent]
    if parent in right:
        right[parent].append(this)
    else:
        right[parent] = [this]
    all_nodes.add(parent)
    all_nodes.add(this)

starts = [node for node in right if node not in left]
nodes = []
for node in starts:
    left[node] = []
    nodes.append(node)

order = ""
current_index = 0
idle_workers = 5
time = 0
schedule = {}

while len(order) < len(all_nodes):
    nodes.sort()
    if len(nodes) > 0 and idle_workers > 0:
        current = nodes[current_index]
        if all((node in order for node in left[current])):
            current_index = 0
            schedule[current] = time + job_time(current)
            idle_workers -= 1
            nodes.remove(current)
        else:
            current_index += 1
    else:
        idle_workers += 1
        if len(schedule) > 0:
            finished_job = min(schedule, key=schedule.get)
            time = schedule.pop(finished_job)
            order += finished_job
            if finished_job in right:
                for child in right[finished_job]:
                    if all((node in order for node in left[child])):
                        nodes.append(child)
print(order)
print(time)
