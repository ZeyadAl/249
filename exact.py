from funcs import *

grch_path = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/GCA_000001405.29/GCA_000001405.29_GRCh38.p14_genomic.fna"
t2t_path = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/GCA_009914755.4/GCA_009914755.4_T2T-CHM13v2.0_genomic.fna"

filename = t2t_path

matches = 0

def process_group(header, lines):
    """Define your processing logic here"""
    global matches
    n = len(lines)
    for i in range(0, n - m + 1):
        if compare(pattern, lines[i:i+m]):
            matches += 1
            print(f"Found match! {header}, start = {i}, end = {i+m-1}")
    
#    print("Processing:", header)  # Example operation
#    print("Number of lines:", len(lines))  # Example operation

def read_groups_streaming(filename):
    with open(filename, 'r') as file:
        header = None
        lines = ""

        for line in file:
            line = line.rstrip().upper()

            if line.startswith(">"):  # New header found
                if header is not None:
                    process_group(header, lines)  # Process previous group
                header = line  # Start a new group
                lines = ""  # Reset the line list
            else:
                lines += line

        if header is not None:
            process_group(header, lines)  # Process the last group

read_groups_streaming(filename)
print(f"num of matches={matches}")
