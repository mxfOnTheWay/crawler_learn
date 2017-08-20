i=1

def col(x):
    global i
  #  print(x)

    if int(x/2)>=3:
        i = i + 1
        return col(int(x/2))

    return i


c=col(500000000)
print(c)
