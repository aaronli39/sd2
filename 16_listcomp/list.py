# Xiaojie(Aaron) Li
# Softdev2 pd8
# K16 -- Do You Even List?
# 2019-04-11

import math

ups, nums = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890"
lows = ups.lower()

# pass word meets minimum threshold?
def minPass(passw):
    upper = [1 for i in passw if i in ups]
    lower = [1 for i in passw if i in lows]
    num = [1 for i in passw if i in nums]
    return len(upper) > 0 and len(lower) > 0 and len(num) > 0

# password strength
def strongPass(passw):
    upper = [1 for i in passw if i in ups]
    lower = [1 for i in passw if i in lows]
    num = [1 for i in passw if i in nums]
    spec = [1 for i in passw if i in ".?!&#,;:-_*"]
    
    upS, lowS, numS, specS = 0, 0, 0, 0
    if len(upper) >= 5: upS = 3
    else: 
        for i in upper: upS += 0.7

    if len(lower) >= 8: lowS = 3.5
    else: 
        for i in upper: lowS += 0.6

    if len(num) >= 5: numS = 4
    else: 
        for i in num: numS += 1.2
    
    if len(spec) >= 5: specS = 1.5
    else: 
        for i in spec: specS += 0.7

    ret = int(math.floor(upS + lowS + numS + specS))
    if ret > 10: return 10
    return ret


print(minPass("asdfA"))
print(strongPass("asdf123aliLIL"))