alpha = "abcdefghijklmnopqrstuvwxyz"
password = "aghfxk5ai5b1cee10z"
shift = 0
decoded = ""

for c in range(len(password)):
    if password[c].isalpha():
        curr = alpha.find(password[c])
        new_shift = curr - shift
        if new_shift < 0:
            decoded += str(alpha[len(alpha) + (new_shift)])
        else:
            decoded += str(alpha[new_shift])
        shift += 1
    else:
        decoded += password[c]
print(decoded)
