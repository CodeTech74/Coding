def mirrored_right_triangle(rows):
    """
    Prints a mirrored right-angled triangle pattern.

    Args:
        rows: The number of rows in the triangle.
    """
    for i in range(rows, 0, -1):  # Iterate from rows down to 1
        print("*" * i)

# Example usage:
rows = 5
mirrored_right_triangle(rows)

rows2 = 10
mirrored_right_triangle(rows2)

rows3 = 3
mirrored_right_triangle(rows3)