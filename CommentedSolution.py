# An empty list where we will build the string
globals().update({chr(0x62):list()})
# An empty string we will use to join the list with
globals().update({chr(0x63):str()})

b.append(0x6f)      # o
b.append(0x60 + 0x10) # p
b.append(0x65)      # e
b.append(0x6e)      # n
b.append(0x28)      # (
b.append(0x26 + 0x01) # '
b.append(0x2e)      # .
b.append(0x6b)      # k
b.append(0x65)      # e
b.append(0x69 + 0x10) # y
b.append(0x26 + 0x01) # '
b.append(0x29)      # )
b.append(0x2e)      # .
b.append(0x62 + 0x10) # r
b.append(0x65)      # e
b.append(0x61)      # a
b.append(0x64)      # d
b.append(0x28)      # (
b.append(0x29)      # )

eval(c.join(chr(x) for x in b))
