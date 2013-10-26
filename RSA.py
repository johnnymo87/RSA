# http://arstechnica.com/security/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/?repost=yes

def RSA_process(n, maxim, repeat):
    # retain original number
    orig = n
    # multiply number by original itself pub times, modulo maximum
    for s in range(repeat - 1):
        n *= orig
        n %= maxim
    return n

def encrypt(string, maxim=91, pub=5):
    # convert letter into UTF-8 decimal number
    nums = [ord(s) for s in string]      
    return [RSA_process(n, maxim, pub) for n in nums]

def decrypt(nums, maxim=91, priv=29):
    chars = [unichr(RSA_process(n, maxim, priv)) for n in nums]
    return ''.join(chars)

# functional test of encrypt
##if encrypt('CLOUD') != [58, 20, 53, 50, 87]:
##    raise Exception('Encrypt logic is incorrect!')
##else:
##    print 'Encrypt logic is correct!'

# functional test of decrypt
##if decrypt([58, 20, 53, 50, 87]) != 'CLOUD':
##    raise Exception('Decrypt logic is incorrect!')
##else:
##    print 'Decrypt logic is correct!'
