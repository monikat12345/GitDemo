wh = 5
while wh >= 1:
    print(wh)
    wh = wh - 1
print("out of while")

wh = 10
while wh >= 1:
    if wh == 6:
        wh = wh-1
        continue ####loop will skip value 6
    if wh == 3:
        break ####loop will break here
    print(wh)
    wh = wh - 1
