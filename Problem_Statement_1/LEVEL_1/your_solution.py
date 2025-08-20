#PS 1, Caesar Cipher
str=input("Input string(can handle capital, small, space, special characters): ")
sft=int(input("Enter Shift (<+shift> for encode, <-shift for decode>): "))
#Modular arithematic is used for cyclicity of functions
def encoding(x):
    if x.isupper() : return chr(65+(ord(x)-65+sft)%26)
    if x.islower() : return chr(97+(ord(x)-97+sft)%26)
    else: return x
enc="".join(map(encoding, str))
print("Encoded Result is:\n ", enc)