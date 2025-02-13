path_pattern = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/DF000000002.fa"
#path_pattern = "/Users/zeyad/Documents/school_stuff/kaust/249/Assignments/1/ncbi_dataset/ncbi_dataset/data/small_pattern"

with open(path_pattern, 'r') as file_pattern:
    pattern = file_pattern.read().upper().replace("\n", "").replace("\r", "")

m = len(pattern)

m1 = m//2
m2  = m - m1

sub_pat1 = pattern[:m1]
sub_pat2 = pattern[m1:]


def compare(pattern, text):
    # if len(pattern) != len(text):
    #     print(f"NOT the same length in compare! pattern = {pattern}, text = {text}")
    #     return False

    for i in range(len(pattern)):
        if pattern[i] != text[i]:
            return False

    return True

def sub_compare(text, sub1 = sub_pat1, sub2 = sub_pat2):
    if (len(sub1) + len(sub2)) != len(text):
        print(f"NOT the same length in sub_compare! sub1 = {sub1}, sub2 = {sub2}, text = {text}")
        return False

    for i in range(len(sub1)):
        if sub1[i] != text[i]:
            # sub1 failed, look into sub2
            for j in range(len(sub2)):
                if sub2[j] != text[m1+j]: # make sure the index is correct
                    return (False,)
            return (True, 2)

    return (True, 1) # do we have to worry if sub2 matched as well? Currently we don't account for it


#def protein(i, text):
    #print(text[i:i+m+2])

def forward_checking(text, pattern = sub_pat2, count = 0):
        # if (len(text) - len(pattern)) > 1:
        #     print("Not the expected sizes in forward checking")
        #     return (False,)

        for i in range(len(pattern)):
            if text[i] != pattern[i]:
                if count > 0:
                    return (False,)
            
                count += 1
            
                if pattern[i] == text[i+1]:
                # we have an insertion
                    # print(f"     insr: text={text}, pat={pattern}, new_text={text[i+1:]}, new_pat={pattern[i:]}, count={count}")
                    return (compare(text=text[i+1:], pattern=pattern[i:]), "insr")
                elif pattern[i+1] == text[i]:
                    # we have a deletion
                    # print(f"     del: text={text}, pat={pattern}, new_text={text[i:]}, new_pat={pattern[i+1:]}, count={count}")
                    return (compare(text=text[i:], pattern=pattern[i+1:]), "del")
                    
                elif pattern[i+1] == text[i+1]:
                    # we have a replacement
                    # print(f"     rep: text={text}, pat={pattern}, new_text={text[i+1:]}, new_pat={pattern[i+1:]}, count={count}")
                    continue
                else:
                    return (False,)

        if count == 0:
            return (True, "exact")
        elif count == 1:
            return (True, "rep")
        else:
            return (False,)

def backward_checking(text, pattern = sub_pat1, count = 0):
        return forward_checking(text[::-1], pattern=pattern[::-1], count=count)
