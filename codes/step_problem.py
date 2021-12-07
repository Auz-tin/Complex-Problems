no_of_steps = int(input("Enter no. of steps:"))
step_rule = [int(entry) for entry in list(input("Enter the list of rules:"))]
steps = [value for value in range(0, no_of_steps + 1)]

print(no_of_steps)
print(step_rule)
print(steps)

probablity_list = []
for step in steps:
    if step != no_of_steps:
        step_probablity = []
        for rule in step_rule:
            next_step = step + rule
            if next_step <= no_of_steps:
                step_probablity.append(next_step)
        probablity_list.append(step_probablity)

print(probablity_list)


def method(step_value):
    for value in probablity_list[step_value]:
        print(step_value, end='step ->')
        print(value, end='->')
        if value == 4:
            print("done")
            global possiblities
            possiblities += 1
            return
        method(value)

possiblities = 0
method(0)

print("Number of possiblities: ",possiblities)
