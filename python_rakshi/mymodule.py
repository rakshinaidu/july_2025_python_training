def checkNumber(num):
    if(num<100):
        raise ValueError("Number should be 100 or greater")
    else:
        print("Number is ok")
