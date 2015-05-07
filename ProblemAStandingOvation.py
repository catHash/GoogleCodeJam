with open('problemAinput3', 'r') as openfileobject:
    i = 0
    for line in openfileobject:
        values = line.split()
        if i == 0:
            T = values[0]
        if i > 0:
            Smax = int(values[0])
            total = 0
            num = 0
            j = 0
            for x in values[1]:
                total = total + int(x)
                if ord(x) == 48:
                    if j < Smax:
                        if total < j+1:
                            num = num + 1
                            total = total + 1
                            #print("zero at position " + str(j) + " total: " + str(total))
                j = j + 1
            #print("Case #: " + str(i) + " Smax: " + str(Smax) + ": " + str(num))
            print("Case #" + str(i) + ": " + str(num))
        i = i + 1
