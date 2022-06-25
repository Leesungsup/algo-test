
def decode():
    for i in range(1,T+1):
        base64=input()
        table = {s: j for j, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
        bit_pattern = ''.join([bin(table[s])[2:].zfill(6) for s in base64])
        text = ''.join([chr(int(bit_pattern[i:i + 8], 2)) for i in range(0, len(bit_pattern), 8)])
        print("#{} {}".format(i,text))
def encode():
    for i in range(1,T+1):
        text=input()
        print(text)
        table = {j: s for j, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
        bit_pattern = ''.join([bin(ord(s))[2:].zfill(8) for s in text])
        print(bit_pattern)
        base64 = ''.join([table[int(bit_pattern[j:j + 6], 2)] for j in range(0, len(bit_pattern), 6)])
        print(base64)
        print("#{} {}".format(i,base64))
T=int(input())
decode()
