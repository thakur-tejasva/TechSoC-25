#I will access a list of 1000 most common english words(I scraped from internet), and find the shift with most english words
print("Warning, pls cd to LEVEL_2 folder before running this code")
with open("words.txt") as f:
    wrds=f.read().casefold().splitlines()#makes a list of most recogonized english words

res=input("Do you want to proceed with test case(a poem) (with shift 3) that my program will find?(y or anything), or custom inut(n or N) (y/n)").lower()
if res=="n":
    str=input("Input encoded string(can handle capital, small, space, special characters, new line), longer is better: ")
else:#Default test case
    with open("test_cases.txt") as f:
        str=f.read()


def encoding(x, sft):#function from ps1 slightly modified
    if x.isupper() : return chr(65+(ord(x)-65+sft)%26)
    elif x.islower() : return chr(97+(ord(x)-97+sft)%26)
    else: return x

def decoded(sft): return "".join(encoding(x, sft) for x in str)#slightly modified from ps1

def score(sft):#scores from maximum no. of recogonisable english words out of list of 1000
    lst=decoded(sft).casefold().split()
    return sum(1 for i in lst if i in wrds)
fsft=max(range(0,-25,-1), key=score)

print(f"\n\nThe shift of encoding was {-fsft}.\n The Decoded result is:\n\n{decoded(fsft)}")