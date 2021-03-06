
class AutoKey(object):
    def encry(self, plaintxt, key):
        cipher = ""
        for i in range(len(plaintxt)):
            if i == 0:
                if (plaintxt[i].isupper()):
                    cipher += chr((ord(plaintxt[i]) + (key) - 65) % 26 + 65)
                else:
                    cipher += chr((ord(plaintxt[i]) + (key) - 97) % 26 + 65)
            else:
                if (plaintxt[i].isupper()):
                    cipher += chr((ord(plaintxt[i]) + (ord(plaintxt[i-1])-65) - 65) % 26 + 65)
                else:
                    cipher += chr((ord(plaintxt[i]) + (ord(plaintxt[i-1])-97) - 97) % 26 + 65)

        return cipher

    def decry(self, cipher, key):
        plaintxt = ""
        for i in range(len(cipher)):
            if i == 0:
                if (cipher[i].isupper()):
                    plaintxt += chr((ord(cipher[i]) - (key) - 65) % 26 + 97)
                else:
                    plaintxt += chr((ord(cipher[i]) - (key) - 97) % 26 + 97)
            else:
                if (cipher[i].isupper()):
                    plaintxt += chr((ord(cipher[i]) - (ord(plaintxt[i-1])-97) - 65) % 26 + 97)
                else:
                    plaintxt += chr((ord(cipher[i]) - (ord(plaintxt[i-1])-97) - 97) % 26 + 97)

        return plaintxt

if __name__ == "__main__":
    print("Nhap ban tin ro: ")
    plt = input()
    print("Nhap Khoa K: ")
    k = int(input())
    C = AutoKey
    print("Ban tin duoc ma hoa: " + C.encry(C, plt, k))