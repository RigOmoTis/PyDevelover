def sort1(t):
    lst = []
    for i in range(len(t)):
        lst.append(t[i])
    lst.sort(key=abs)
    return(lst)

tpl = (-2, 69, 420, -666, 4, 36, 0, 57)
print(tpl,"\n",sort1(tpl))