thickness = 3
mark = 'D'

hh = thickness + 3  ### Half of the height with center (odd)
i = -hh
while i <= hh:
    sw = thickness * 4 + 3 - abs(i)  ### Max wide of the stroke
    if sw > thickness * 4:
        sw = thickness * 4
    j = 0
    for j in range(sw):
        if abs(i) - (thickness // 2 + 1) >= hh - thickness:
            print(mark, end='')  ### Top and Bottom
        elif (j > thickness - 1) and (j < sw - thickness):
            print(' ', end='')  ### Gaps
        else:
            print(mark, end='')  ### Sides
    print('\r')
    i += 1
