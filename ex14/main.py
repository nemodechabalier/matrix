import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix
from projection import projection


def write_proj(matrix : Matrix, filepath):
    with open(filepath, 'w') as f:
        n = len(matrix.data)
        for col in range(n):
            row_values = [str(matrix.data[row][col]) for row in range(n)]
            f.write(", ".join(row_values) + "\n")

def main():
    proj = projection()
    print(proj)
    write_proj(proj, "matrix_display/proj")
	
if __name__ == "__main__":
	main()