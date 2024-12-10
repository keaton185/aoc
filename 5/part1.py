def process_update(update, rule) -> int:
    read = set()
    for n in update:
        if n in rule and len(rule[n].intersection(read)) > 0:
            return 0
        read.add(n)
    middle = update[len(update) // 2]
    return middle

def main() -> int:
    input = open("input.txt").read()
    result = 0
    rules = {}

    for line in input.strip().split('\n'):
        if line == '':
            continue
        if '|' in line:
            a, b = [int(x) for x in line.strip().split("|")]
            if a not in rules:
                rules[a] = set()
            rules[a].add(b)
        else:
            update = [int(x) for x in line.strip().split(",")]
            result += process_update(update, rules)

    return result

if __name__ == '__main__':
    result = main()
    # test_answer = 143
    print(f"The answer is: {result}")