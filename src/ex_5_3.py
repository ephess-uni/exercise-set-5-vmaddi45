""" ex_5_3.py
This module contains an entry point that:

- creates a CLI that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation of 1
- writes the processed data to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

def main(infile, outfile):
    # Load data from the input file into a numpy array
    data = np.loadtxt(infile, delimiter=',')

    # Shift and scale the data to have a mean of 0 and standard deviation of 1
    processed_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # Save the processed data to the output file
    np.savetxt(outfile, processed_data, delimiter=',')

if __name__ == "__main__":
    # Create an argument parser object
    parser = ArgumentParser(description="This program processes data by shifting and scaling to a mean of 0 and a standard deviation of 1.")

    # Add positional arguments for input and output filenames
    parser.add_argument("infile", help="Input filename for the data to be processed.")
    parser.add_argument("outfile", help="Output filename for the processed data.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the provided filenames
    main(args.infile, args.outfile)
