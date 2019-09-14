def tct(num):
    try:
        r = 1/num
    except:
        print('exception caught ')
        return
    return r
print(tct(10))
print(tct(0))
