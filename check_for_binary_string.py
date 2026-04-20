def isBinary(s):
    for ch in s:
        if ch not in ('0', '1'):
            return False
    return True
