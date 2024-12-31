# Find all combinations for right-angled triangles with float numbers

import math

limit = 20  # Set the upper limit for numbers
step = 0.5  # Set the step size for float increments
tolerance = 1e-6  # Allowable tolerance for float comparisons
triangles = []

a = 1.0
while a < limit:
    b = a + step
    while b < limit:
        c = b + step
        while c < limit:
            if math.isclose(a**2 + b**2, c**2, rel_tol=tolerance):
                triangles.append((round(a, 2), round(b, 2), round(c, 2)))
            c += step
        b += step
    a += step

# Print results
print("Right-angled triangles with float numbers:", triangles)


"""Output:
Right-angled triangles with float numbers: [(1.5, 2.0, 2.5), (2.5, 6.0, 6.5), (3.0, 4.0, 5.0), (3.5, 12.0, 12.5), (4.0, 7.5, 8.5), 
(4.5, 6.0, 7.5), (5.0, 12.0, 13.0), (6.0, 8.0, 10.0), (6.0, 17.5, 18.5), (7.5, 10.0, 12.5), (7.5, 18.0, 19.5), (8.0, 15.0, 17.0), 
(9.0, 12.0, 15.0), (10.0, 10.5, 14.5), (10.5, 14.0, 17.5)]
"""