from ast import literal_eval

def get_part_sum(part):
    part_sum = 0
    for value in part.values():
        part_sum += value
    return part_sum

def is_accepted(workflows, part):
    current = "in"
    while current != "A" and current != "R":
        for (condition, dest) in workflows[current]:
            if condition is None or (condition[1] == ">" and part[condition[0]] > condition[2]) \
                or (condition[1] == "<" and part[condition[0]] < condition[2]):
                current = dest
                break

    return current == 'A'

def onestar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    new_line = False
    workflows = dict()

    for line in lines:
        line = line.strip()
        if not line:
            new_line = True

        else:
            if not new_line:
                line = line.split("{")
                w_name = line[0]
                rules = line[1][:-1].split(",")
                formatted_rules = []
                for rule in rules:
                    if "<" in rule or ">" in rule:
                        condition = rule.split(":")[0]
                        condition_var = condition[0]
                        condition_sign = condition[1]
                        condition_value = int(condition[2:])
                        dest = rule.split(":")[1]
                        formatted_rules.append(((condition_var, condition_sign, condition_value), dest))
                    else:
                        formatted_rules.append((None, rule))    

                workflows[w_name] = formatted_rules
            else:
                values = line[1:-1].split(",")
                part = dict()
                for value in values:
                    part[value[0]] = int(value.split("=")[1])
    
                if is_accepted(workflows, part):
                    total += get_part_sum(part)

    print(total)

onestar_solution()
            