def main():
    list1 = []
    list2 = []    
    with open('input.txt', 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))

    counts = {}
    for num in list1:
        counts[num] = list2.count(num)
    similarity_score = 0
    for num in list1:
        similarity_score += num * counts[num]

    print(similarity_score)
if __name__ == '__main__':
    main()