data = int(input())
up = data/100
down = data % 100
if(1 <= up and up <= 12):
    if(1 <= down and down <= 12):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if(1 <= down and down <= 12):
        print("YYMM")
    else:
        print("NA")
