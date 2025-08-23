#PS 1, Caesar Cipher
#Test case or custom input
print("Warning, pls cd to LEVEL_1 folder before running this code")
res=input("Do you want to proceed with test case(a poem) with shift 3?(y or anything), or custom inut(n or N) (y/n)").lower()
if res=="n":
    str=input("Input string(can handle capital, small, space, special characters): ")
    sft=int(input("Enter Shift (<+shift> for encode, <-shift for decode>): "))
else:
    with open("test_cases.txt") as f:
        str=f.read()
    sft= 3
#Modular arithematic is used for cyclicity of functions
def encoding(x):
    if x.isupper() : return chr(65+(ord(x)-65+sft)%26)
    if x.islower() : return chr(97+(ord(x)-97+sft)%26)
    else: return x
enc="".join(map(encoding, str))
print("Original string is:\n\ny", str)
print("\n\nEncoded Result is:\n", enc)