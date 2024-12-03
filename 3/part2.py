import re

mul_pattern = re.compile(r"mul\(\d{0,3},\d{0,3}\)")
num_pattern = re.compile(r"\d+")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

def main():
    result = 0
    operations_enabled = True
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        joined_lines = ''.join(lines).rstrip()
        
        tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d{0,3},\d{0,3}\))", joined_lines)
        
        for token in tokens:
            token = token.rstrip()
            if not token:
                continue
            
            if token == "don't()":
                operations_enabled=False
            if token == "do()":
                operations_enabled=True
            elif operations_enabled and mul_pattern.match(token):
                nums = num_pattern.findall(token)
                print(nums)
                result += int(nums[0]) * int(nums[1])

    print(result)

if __name__ == '__main__':
    main()