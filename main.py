import random
import json

def print_grid(grid):
    print("\n".join(" ".join(str(num) if num != 0 else '.' for num in row) for row in grid))
    print()

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    if num in (grid[r][col] for r in range(9)):
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty_location(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True
    row, col = empty_location
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    fill_grid(grid)
    remove_numbers(grid)
    return grid

def fill_grid(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num
                        if fill_grid(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True

def remove_numbers(grid, num_remove=40):
    count = 0
    while count < num_remove:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if grid[r][c] != 0:
            grid[r][c] = 0
            count += 1

def is_complete(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return False
    return True

def save_puzzle(grid, filename):
    with open(filename, 'w') as f:
        json.dump(grid, f)
    print(f"Puzzle saved to {filename}")

def load_puzzle(filename):
    try:
        with open(filename, 'r') as f:
            grid = json.load(f)
        return grid
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

def validate_puzzle(grid):
    for r in range(9):
        for c in range(9):
            num = grid[r][c]
            if num != 0 and not is_valid(grid, r, c, num):
                return False
    return True

def main():
    print("Sudoku Solver and Generator")
    choice = input("Choose (1) Solve a Sudoku, (2) Generate a Sudoku puzzle, (3) Load a Sudoku puzzle, (4) Save the current puzzle: ")
    
    if choice == '1':
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        if solve_sudoku(grid):
            print("Sudoku solved successfully:")
            print_grid(grid)
        else:
            print("No solution exists")
    elif choice == '2':
        grid = generate_sudoku()
        print("Generated Sudoku puzzle:")
        print_grid(grid)
        input("Press Enter to solve the generated puzzle...")
        if solve_sudoku(grid):
            print("Solved Sudoku puzzle:")
            print_grid(grid)
        else:
            print("No solution exists")
    elif choice == '3':
        filename = input("Enter the filename to load: ")
        grid = load_puzzle(filename)
        if grid and validate_puzzle(grid):
            print("Loaded Sudoku puzzle:")
            print_grid(grid)
            if solve_sudoku(grid):
                print("Solved Sudoku puzzle:")
                print_grid(grid)
            else:
                print("No solution exists")
        else:
            print("Invalid puzzle or file error.")
    elif choice == '4':
        filename = input("Enter the filename to save the puzzle: ")
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        save_puzzle(grid, filename)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
