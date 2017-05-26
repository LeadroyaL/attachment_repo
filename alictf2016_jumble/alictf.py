import alictf_data

from Crypto.Cipher import AES, ARC4

rc4_key = alictf_data.rc4_key
aes_key = alictf_data.aes_key
target = alictf_data.target
xor_13 = 0x13
bde_list = alictf_data.bde_list

# xor with 0x13
for i in range(32):
    target[i] ^= xor_13
print ''.join(chr(i) for i in target).encode('hex')
# 4c3ac171844edf54d61cc0f8176d9e099a4cbc9c0ca12843bbbbcc9f11fe10f2

# target[0:16] AES_decrypt
cipher = AES.new(''.join(chr(i) for i in aes_key), AES.MODE_ECB)
aes_dec = cipher.decrypt(''.join(chr(i) for i in target[0:16]))
print aes_dec.encode('hex')
# eee13b8e3382258ee7c2fbb7d71b3932
for i in range(16):
    target[i] = ord(aes_dec[i])

# target[16:32] -= index
for i in range(16, 32):
    target[i] = (target[i] - i) & 0xff

# rc4 decrypt
cipher = ARC4.new(''.join(chr(i) for i in rc4_key))
rc4_dec = cipher.decrypt(''.join(chr(i) for i in target[0:32]))
print rc4_dec.encode('hex')
# 998564a1e7a3e50c301aee25f319c9a9b020f94d22d7cc000000000000000000
target = rc4_dec.rstrip('\0')
target = [ord(i) for i in target]


def b_decrypt(in_data):
    size = len(in_data)
    for ii in range(size - 1, -1, -1):
        if ii == 0:
            in_data[ii] = (in_data[ii] - in_data[size - 1]) & 0xff
        else:
            in_data[ii] = (in_data[ii] - in_data[ii - 1]) & 0xff
        in_data[ii] = (in_data[ii] - 58) & 0xff
    return in_data


def d_decrypt(in_data):
    size = len(in_data)
    for ii in range(size - 1, -1, -1):
        if ii == 0:
            in_data[ii] = (in_data[ii] ^ in_data[size - 1]) & 0xff
        else:
            in_data[ii] = (in_data[ii] ^ in_data[ii - 1]) & 0xff
        in_data[ii] ^= 150
    return in_data


def e_decrypt(in_data):
    size = len(in_data)
    for ii in range(size):
        in_data[ii] = ((in_data[ii] & 0xf) << 4) | ((in_data[ii] & 0xf0) >> 4)
    return in_data

# java decrypt
bde_list = bde_list[::-1]
for i in range(len(bde_list)):
    cur = bde_list[i]
    if cur == 'b':
        target = b_decrypt(target)
    elif cur == 'd':
        target = d_decrypt(target)
    elif cur == 'e':
        target = e_decrypt(target)
    else:
        print "ERROR"

print target
print ''.join(chr(i) for i in target)

# CTF{Y0u_Ar3_Go0d_a7_1t}