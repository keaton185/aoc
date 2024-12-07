DIRECTIONS = [
    (0, 1), # right
    (0, -1), # left
    (1, 0), # down
    (-1, 0), # up
    (1, 1), # down right
    (-1, -1), # up left
    (1, -1), # down left
    (-1, 1), # up right
]

def get_input() -> str:
    with open('input.txt') as f:
        return f.read()
    
def build_grid(input: str) -> list[list[str]]:
    rows = input.strip().splitlines()
    return [list(row) for row in rows]

def is_within_bounds(array: list[list[str]], i: int, j: int) -> bool:
    return i >= 0 and i < len(array) and j >= 0 and j < len(array[0])

def count_word(grid: list[list[str]], word: str) -> int:
    word_length = len(word)
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for dr, dc in DIRECTIONS:
                if all(
                    is_within_bounds(grid, i + k * dr, j + k * dc) and
                    grid[i + k * dr][j + k * dc] == word[k]
                    for k in range(word_length)
                ):
                    count += 1
    return count

def main():
    input = get_input()
    grid = build_grid(input)
    occurrences = count_word(grid, 'XMAS')
    print(occurrences)

if __name__ == '__main__':
    main()