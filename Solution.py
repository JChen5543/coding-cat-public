def countRepeat(a, b):
    for x in (len(a) - 1):
        if a[x + 1] == b:
            count += 1
            
    return count