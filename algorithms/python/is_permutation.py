# Time complexity: O(n)
def is_permutation(word1, word2):
    chars1 = dict()
    chars2 = dict()

    for char in word1:
        if not chars1.get(char):
            chars1[char] = 1
        else:
            chars1[char] = chars1.get(char) + 1        

    for char in word2:
        if not chars2.get(char):
            chars2[char] = 1
        else:
            chars2[char] = chars2.get(char) + 1

    if len(chars1) != len(chars2):
        return False

    for char in chars1:
        if chars1.get(char) != chars2.get(char):
            return False
    
    return True
