
def onestar_solution(label):
    current_value = 0
    for c in label:
        current_value+=ord(c)
        current_value*=17
        current_value%=256
    
    return current_value

def bothstars_solution():
    file = open('input', 'r')
    lines = file.readlines()
    total = 0

    boxes = [[] for i in range(256)]
    
    for value in lines[0].split(","):
        if value[-1] == "-":
            label = value[0:-1]
            box = onestar_solution(label)
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box].pop(i)
                    break
        else:
            label = value[0:-2]
            focal_length = int(value[-1])
            box = onestar_solution(label)
            found = False
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    found = True
                    boxes[box][i][1] = focal_length

            if not found:
                 boxes[box].append([label, focal_length])
           
    total = 0
    for i in range(256):
        for j in range(len(boxes[i])):
            total += (i+1) * (j+1) * boxes[i][j][1]
    print(total)

bothstars_solution()