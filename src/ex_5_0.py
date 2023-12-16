"""ex_5_0.py"""

def line_count(infile):
    try:
        # Open the file in read mode
        with open(infile, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()

            # Count the number of lines
            num_lines = len(lines)

            # Print the result
            print(f'The number of lines in {infile} is: {num_lines}')
    except FileNotFoundError:
        print(f"Error: The file '{infile}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
