


def main():
    list1 = []
    list2 = []
    distances = []
    with open('input.txt', 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        distances.append(abs(list1[i] - list2[i]))

    print(sum(distances))    
    
if __name__ == '__main__':
    main()