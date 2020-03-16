import simplecrypt

f = open('output.txt','w')
with open('encrypted.bin','rb') as inb:
    encrypted = inb.read()
with open('passwords.txt','r') as inp:
    passwords = inp.read().strip().split('\n')
for i in range(len(passwords)):
    try:
        f.write(simplecrypt.decrypt(passwords[i],encrypted))
    except simplecrypt.DecryptionException:
        continue
    else:
        break
