# Time complexity: O(n)
def is_unique(string):
    chars = dict()

    for char in string:
        if chars.get(char) == 1:
            return False
        
        chars[char] = 1
    
    return True
