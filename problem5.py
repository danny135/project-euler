num = 1
found = False
while not found:
    for i in range(2,21):
        if num % i != 0:
            print str(num) + " not " + str(i) + " divisible"
            break
        if i == 20:
            found = True
            print "FOUND"
    num += 1
print num

