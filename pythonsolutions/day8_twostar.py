import math

def two_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    # Make a directed graph using the input and then rely on the movement instructions to traverse it.
    # Don't need anything more than just a map between the node and its left/right nodes.

    instructions = lines[0].strip()
    node_mapping = {}

    # Make the mapping that represents the graph; just like an adjacency list.
    for line in lines[2:]:
        values = line.split("=")
        node = values[0].strip()
        pair = values[1].split(",")

        left = pair[0][2:].strip()
        right = pair[1].strip()[0:-1]
        node_mapping[node] = [left, right]


    # Process the instructions
    a_nodes = [key for key in node_mapping.keys() if key.endswith("A")]
    multiples = []
    for a_node in a_nodes:
        end_found = False
        instruction_index = 0
        current_node = a_node
        steps_taken = 0

        while not end_found:
            if instructions[instruction_index] == "L":
                current_node = node_mapping[current_node][0]
            else:
                current_node = node_mapping[current_node][1]

            steps_taken += 1
            if current_node.endswith("Z"):
                end_found = True

            instruction_index = (instruction_index + 1) % (len(instructions))

        multiples.append(steps_taken)
    
    common_steps = math.lcm(*multiples)
    print(common_steps)

two_star_solution()