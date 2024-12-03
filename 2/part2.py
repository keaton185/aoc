def calculate_differences(levels):
    return [levels[i] - levels[i - 1] for i in range(1, len(levels))]

def is_safe_sequence(differences):
    safe_positive = {1, 2, 3}
    safe_negative = {-1, -2, -3}
    return set(differences).issubset(safe_positive) or set(differences).issubset(safe_negative)

def is_any_subrow_safe(row):
    for i in range(len(row)):
        subrow = row[:i] + row[i + 1:]
        differences = calculate_differences(subrow)
        if is_safe_sequence(differences):
            return True
    return False

def main():
    safe_reports = 0
    
    with open('input.txt', 'r') as f:
        for line in f:
            levels = list(map(int, line.split()))
            if is_any_subrow_safe(levels):
                safe_reports += 1
    
    print(safe_reports)

if __name__ == '__main__':
    main()