import random

def generate_dungeon(h=15, w=30):
    grid = [["#"]*w for _ in range(h)]
    # Procedurally place random rooms
    for _ in range(5):
        rh, rw = random.randint(3, 5), random.randint(5, 8)
        rx, ry = random.randint(1, w - rw - 1), random.randint(1, h - rh - 1)
        for r in range(ry, ry + rh):
            for c in range(rx, rx + rw):
                grid[r][c] = "."
    return grid

def print_dungeon(grid):
    for row in grid:
        print("".join(row))

def main():
    print("Generating rogue-like procedurally-generated grid layout:")
    grid = generate_dungeon()
    print_dungeon(grid)

if __name__ == "__main__":
    main()
