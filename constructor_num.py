constructor = []

def d(n):
    if n < 10000:
        constructor.append(n)

    if n < 10:
        a = 2*n
        return d(a)
    elif n < 100:
        a = (n//10)*11 + (n%10)*2
        return d(a)
    elif n < 1000:
        a = (n//100)*101 + ((n%100)//10)*11 + ((n%100)%10)*2
        return d(a)
    elif n < 10000:
        a = (n//1000)*1001 + ((n%1000)//100)*101 + (((n%1000)%100)//10)*11 + (((n%1000)%100)%10)*2
        return d(a)

    return constructor
