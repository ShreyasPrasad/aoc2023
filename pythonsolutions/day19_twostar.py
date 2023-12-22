import copy

def twostar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    workflows = dict()

    for line in lines:
        line = line.strip()
        if not line:
            break
        
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

    work = []
    # The valid ranges for our current search in the specified workflow.
    ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    work_item = ("in", ranges)
    work.append(work_item)

    total = 0
    while work:
        (workflow, ranges) = work.pop()
        print(workflow)
        print(ranges)
        if workflow == "A":
            mult = 1
            for range in ranges.values():
                mult *= max(0, (range[1] - range[0] + 1))
            total += mult
            continue
        elif workflow == "R":
            continue

        # Modify the ranges we are looking at as we go, for each rule that we encounter
        for (condition, dest) in workflows[workflow]:
            ranges_copy = copy.deepcopy(ranges)
            if condition is None:
                work.append((dest, ranges_copy))
            else:
                if condition[1] == ">" and ranges[condition[0]][1] > condition[2] and condition[2] + 1 <= 4000:
                    ranges_copy[condition[0]][0] = condition[2] + 1
                    ranges[condition[0]][1] = condition[2]
                    work.append((dest, ranges_copy))
                elif condition[1] == "<" and ranges[condition[0]][0] < condition[2] and condition[2] - 1 >= 1:
                    ranges_copy[condition[0]][1] = condition[2] - 1
                    ranges[condition[0]][0] = condition[2]
                    work.append((dest, ranges_copy))

                if ranges[condition[0]][0] > ranges[condition[0]][1]:
                    break
    print(total)


twostar_solution()