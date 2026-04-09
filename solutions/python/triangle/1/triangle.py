def equilateral(sides):
    a, b, c = sides
    
    return a == b == c == a and not 0 in sides
    
def isosceles(sides):
    a, b, c = sides
    
    if 0 in sides:
        return False
    return a == b and a + b > c or b == c and b + c > a or c == a and a + c > b

def scalene(sides):
    a, b, c = sides

    if 0 in sides:
        return False
    if a > b + c or b > c + a or c > a + b:
        return False
    else:
        return a != b != c != a and not 0 in sides