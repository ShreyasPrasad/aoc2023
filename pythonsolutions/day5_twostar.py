class CategoryMapping:

    def __init__(self):
        # A mapping is formatted as [start, end, range]
        self.mappings = []

    def add_mapping(self, mapping_line):
        numbers = mapping_line.split()
        self.mappings.append([int(numbers[1]), int(numbers[0]), int(numbers[2])])

    def sort_mappings(self):
        def comparator(item):
            return item[0]
        self.mappings.sort(key=comparator)

    def get_child_intervals(self, interval):
        child_intervals = []
        interval_start = interval.start
        interval_end = interval.end
        next = interval.category + 1

        last_end = interval_start

        for mapping in self.mappings:
            start = mapping[0]
            end = mapping[0] + mapping[2]
            if start >= interval_start and start < interval_end:
                child_intervals.append(Interval(mapping[1], (min(interval_end, end) - start) + mapping[1], next))
                if start > last_end:
                    child_intervals.append(Interval(last_end, start, next))
                last_end = min(interval_end, end)
            elif start < interval_start and end > interval_start:
                child_intervals.append(Interval((interval_start - start) + mapping[1], (min(interval_end, end) - start) + mapping[1], next))
                last_end = min(interval_end, end)
            
        if last_end < interval_end:
            child_intervals.append(Interval(last_end, interval_end, next))

        return child_intervals
        

class Interval:
    
    def __init__ (self, start, end, category):
        self.start = start
        self.end = end
        self.category = category

def two_star_solution():
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

    for category in categories:
        category.sort_mappings()

    """
    Each seed range is an interval. The interval results in other intervals to process,
    level by level for each mapping.
    """
    cat_queue = []
    min_location_number = 0
    for i in range(len(seeds)):
        if i%2 == 0:
            cat_queue.append(Interval(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]), 0))
    
    while cat_queue:
        next = cat_queue.pop(0)
        if next.category == 7:
            if not min_location_number or next.start < min_location_number:
                min_location_number = next.start
        else:
            for interval in categories[next.category].get_child_intervals(next):
                cat_queue.append(interval)
    
    print(min_location_number)

two_star_solution()