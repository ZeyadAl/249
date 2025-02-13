from funcs import *
import pysam
import io

grch_path = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/GCA_000001405.29/GCA_000001405.29_GRCh38.p14_genomic.fna.gz"
t2t_path = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/GCA_009914755.4/GCA_009914755.4_T2T-CHM13v2.0_genomic.fna.gz"

filename = t2t_path

offby1_matches = 0

def process_group(header, text):
    global offby1_matches
    n = len(text)
    for i in range(0, n - m + 1):
        # compare text[i:i+m] and pattern
        result = sub_compare(text[i:i+m])
        if result[0]:
            if result[1] == 1:
                # we have to go forward
                # print(f"loc = {i}, str = {text[i:i+m]}, match_sub? = {result[1]}, sub1={sub_pat1}, rem_sub = {text[i+m1:i+m]}, sub2={sub_pat2}")
                result_forward = forward_checking(text[i+m1:i+m+1])
                if result_forward[0]:
                    offby1_matches += 1
                    print(f"{header}, loc={i}, kind={result_forward[1]}")
            else:
                # print(f"loc = {i}, str = {text[i:i+m]}, match_sub? = {result[1]}, sub2={sub_pat2}, rem_sub = {text[i:i+m1]}, sub1={sub_pat1}")
                result_backward = backward_checking(text[i-1:i+m1])
                if result_backward[0]:
                    offby1_matches += 1
                    print(f"{header}, loc={i}, kind={result_backward[1]}")
    
def read_groups_streaming(filename):
    with pysam.BGZFile(filename, 'r') as bgzf_file:
        with io.TextIOWrapper(bgzf_file) as file:
            header = None
            lines = ""
            for line in file:
                line = line.rstrip().upper()
                if line.startswith(">"):  # header
                    if header is not None:
                        process_group(header, lines)  # process
                    header = line  # new group
                    lines = ""  # reset
                else:
                    lines += line
            if header is not None:
                process_group(header, lines)  # last group

read_groups_streaming(filename)
print(f"num of offby1_matches={offby1_matches}")
