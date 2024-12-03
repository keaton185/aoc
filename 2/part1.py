def calculate_differences(levels):
    return [levels[i] - levels[i - 1] for i in range(1, len(levels))]

def is_safe_sequence(differences):
    safe_positive = {1, 2, 3}
    safe_negative = {-1, -2, -3}
    return set(differences).issubset(safe_positive) or set(differences).issubset(safe_negative)

def main():
    safe_reports = 0
    
    with open('input.txt', 'r') as f:
        for line in f:
            levels = list(map(int, line.split()))
            differences = calculate_differences(levels)
            if is_safe_sequence(differences):
                safe_reports += 1
    
    print(safe_reports)
    
    
if __name__ == '__main__':
    main()