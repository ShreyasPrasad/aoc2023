class CategoryMapping:

    def __init__(self):
        # A mapping is formatted as [start, end, range]
        self.mappings = []

    def add_mapping(self, mapping_line):
        numbers = mapping_line.split()
        self.mappings.append([int(numbers[1]), int(numbers[0]), int(numbers[2])])

    def get_mapping(self, starting):
        for mapping in self.mappings:
            if starting >= mapping[0] and (starting < mapping[0] + mapping[2]):
                return mapping[1] + (starting - mapping[0])
        
        return starting



def one_star_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    # Get the seeds
    seeds = lines[0][(lines[0].find(":") + 1):].split()

    categories = [CategoryMapping() for i in range(7)]
    lines = lines[1:]
    
    # Make the categories
    current_category = 0
    for line in lines:
        if "soil-to-fertilizer" in line:
            current_category = 1
        elif "fertiziler-to-water" in line:
            current_category = 2
        elif "water-to-light" in line:
            current_category = 3
        elif "light-to-temperature" in line:
            current_category = 4
        elif "temperature-to-humidity" in line:
            current_category = 5
        elif "humidity-to-location" in line:
            current_category = 6
        
        if len(line.split()) == 3:
            categories[current_category].add_mapping(line)

    # Process the seeds
    min_location_number = 0
    for seed in seeds:
        value = int(seed)
        for category in categories:
            value = category.get_mapping(value)
        
        if not min_location_number or value < min_location_number:
            min_location_number = value
    
    print(min_location_number)

one_star_solution()