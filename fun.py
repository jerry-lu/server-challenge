# Implement modulo without using the (%) operator.
def modulo(a, b):
    return a - (b * (a//b))

# Take an input string and determine if exactly 3 question marks 
# exist between every pair of numbers that add up to 10.
# If so, return true, otherwise return false. 
def question_mark(s):
    numbers = {c:i for i,c in enumerate(s) if c.isdigit()}
    # list containing indices of numbers which add to 10
    pairs = []
    for a, b in numbers.items():
        for c, d in numbers.items():
            if  b != d and int(a) + int(c) == 10:
                pairs.append((b, d))
    if not pairs:
        return False
    # iterate through pairs and check if they contain 3 question marks
    for x, y in pairs:
        substr = s[x+1:y]
        if substr.count('?') == 3:
            return True
    return False