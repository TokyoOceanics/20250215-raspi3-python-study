#!
#2024/11/17
#インターフェース2022年11月号 付録
#
def caesar(n, message):

    def shift(c, n, start, end):
        return chr((ord(c)-start+n) %
            (end-start+1)+start)
    return ''.join([shift(c, n, 0x20, 0x7e) for c in message])

original='Programming'

encrypted=caesar(2, original)
decrypted=caesar(-2, encrypted)
print(f'平文={original}\n 暗号文={encrypted}\n復号された文={decrypted}')
    
    