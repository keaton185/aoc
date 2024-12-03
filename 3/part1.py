import re

mul_pattern = re.compile(r"mul\(\d{0,3},\d{0,3}\)")
num_pattern = re.compile(r"\d+")


def main():
    result = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        joined_lines = ''.join(lines).rstrip()
        muls = mul_pattern.findall(joined_lines)
        for mul in muls:
            nums = num_pattern.findall(mul)
            result += int(nums[0]) * int(nums[1])
            
    print(result)

if __name__ == '__main__':
    main()