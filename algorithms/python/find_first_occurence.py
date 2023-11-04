def first_occurence(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0

    index = -1
    needleLen = len(needle)

    i = 0
    while (i < len(haystack)):
        if haystack[i:i+needleLen] == needle:
            return i
        
        i += 1

    return index
