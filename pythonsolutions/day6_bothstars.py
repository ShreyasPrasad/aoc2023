def both_stars_solution():
    file = open('input', 'r')
    total = 0
    lines = file.readlines()

    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()

    total = 1

    for i in range(len(times)):
        time = int(times[i])
        combo = 0
        for j in range(time+1):
            speed = j
            distance = speed * (time-j)
            if distance > int(distances[i]):
                combo += 1
        if combo > 0:
            total *= combo

    print(total)

both_stars_solution()