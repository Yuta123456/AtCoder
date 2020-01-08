piano = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
sound = ["Do","Re","Mi","Fa","So","La","Si"]
s = input()
start = 0
while True:
    for i in range(len(s)):
        if piano[i + start] != s[i]:
            start += 1
            break
        if i == len(s) - 1:
            q = 0
            for j in range(start):
                if piano[j] == "W":
                    q += 1
            print(sound[q%7])
            exit()
