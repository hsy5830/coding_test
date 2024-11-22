credit, grade = 0, 0
cal = {'+':0.5, '0':0}
cal2 = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
while 1:
    try:
        s, c, g = input().split()
        if g == 'P': continue
        elif g == 'F':
            credit += float(c)
        else:
            credit += float(c)
            grade += (cal2[g[0]] + cal[g[1]]) * float(c)
    except:
        break

print(grade/credit)