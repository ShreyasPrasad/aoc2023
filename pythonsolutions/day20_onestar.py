def get_state_key(module_map):
    state = ""
    for module_name in module_map.keys():
        state += (module_name + "#" + module_map[module_name][-1] + "@")

def onestar_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    module_map = dict()

    for line in lines:
        line = line.strip()
        module_name = line.split("->")[0][:-1]
        if module_name[0] == '%':
            module_type = 'F'
            module_name = module_name[1:]
        elif module_name[0] == '&':
            module_type = 'C'
            module_name = module_name[1:]
        else:
            module_type = 'B'
        
        dests = line.split("->")[1].replace(" ", "").split(",")

        if module_type == 'C':
            # Conjunction modules must know their parents.
            module_map[module_name] = [module_type, dests, {}, "HIGH"]
        else:
            # Flip-flop modules start as OFF by default.
            module_map[module_name] = [module_type, dests, "OFF"]

    # Assign conjunction modules their parents.
    for module_name in module_map.keys():
        for dest in module_map[module_name][1]:
            if dest in module_map and module_map[dest][0] == 'C':
                module_map[dest][2][module_name] = "LOW"
    
    pulses = []
    # state_map = set()
    # state_map.add(get_state_key(module_map))

    low_pulses = 0
    high_pulses = 0
    presses = 0
    while presses < 4000:
        pulses.append(("button", "broadcaster", "LOW"))
        presses += 1
        while pulses:
            (source, current, pulse) = pulses.pop(0)
            if pulse == "HIGH":
                high_pulses += 1
            else:
                low_pulses += 1
            # Handle the button press
            if source == "button":
                for dest in module_map[current][1]:
                    pulses.append((current, dest, pulse))
            # Handle untyped modules
            elif current not in module_map:
                continue
            # Handle conjunction modules
            elif module_map[current][0] == 'C':
                num_high = 0
                for last_seen in module_map[current][2].keys():
                    if last_seen == source:
                        module_map[current][2][last_seen] = pulse
                    if module_map[current][2][last_seen] == "HIGH":
                        num_high += 1

                # Send a HIGH pulse unless all inputs are remembered to be HIGH
                new_pulse = "HIGH"
                if num_high == len(module_map[current][2]):
                    new_pulse = "LOW"

                if current in ["bm"] and new_pulse == "HIGH":
                    print(f"{current} sending HIGH after {presses} presses for {current}.")
                
                module_map[current][-1] = new_pulse
                for dest in module_map[current][1]:
                    pulses.append((current, dest, new_pulse))
            # Handle flip-flop modules
            else:
                if pulse == "HIGH":
                    continue
                if module_map[current][-1] == "ON":
                    new_pulse = "LOW"
                    module_map[current][-1] = "OFF"
                else:
                    module_map[current][-1] = "ON"
                    new_pulse = "HIGH"
                for dest in module_map[current][1]:
                    pulses.append((current, dest, new_pulse))

onestar_solution()