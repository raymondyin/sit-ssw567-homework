def classify_triangle(a, b, c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


    """
    if a == 0 or b == 0 or c == 0:
        return 'NotATriangle'

    if a == b and b == c and a == c:
        return "equilateral"
    else:
        lst = [a, b, c]
        lst.sort()
        if lst[0] + lst[1] <= lst[2]:
            return "NotATriangle"
        if lst[0] == lst[1] or lst[1] == lst[2]:
            return "isoceles"
        elif lst[0]**2 + lst[1]**2  == lst[2]**2:
            return "right"
        else:
            return 'scalene'


if __name__ == '__main__':
    # examples of running the code
    pass
