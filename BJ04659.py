from sys import stdin

vowels = "aeiou"

while True:
    ipt = stdin.readline().rstrip()
    if ipt == "end": break

    acceptable = True
    cnt_seq, prev_vowel, has_vowel = 1, False, False

    if ipt[0] in vowels:
        has_vowel = True
        prev_vowel = True

    for i in range(1, len(ipt)):
        curr = ipt[i]
        if curr in vowels:
            has_vowel = True
            if prev_vowel:
                cnt_seq += 1
            else:
                prev_vowel = True
                cnt_seq = 1
        else:
            if prev_vowel:
                prev_vowel = False
                cnt_seq = 1
            else:
                cnt_seq += 1

        if ipt[i-1] == ipt[i] and ipt[i] != "e" and ipt[i] != "o":
            acceptable = False
            break

        if cnt_seq >= 3:
            acceptable = False
            break

    if not has_vowel:
        acceptable = False

    if acceptable:
        print("<" + ipt + "> is acceptable.")
    else:
        print("<" + ipt + "> is not acceptable.")
