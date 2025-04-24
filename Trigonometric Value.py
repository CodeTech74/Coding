import math

def calculate_trigonometric_values(angle_degrees):
  """
  Calculates the sine, cosine, and tangent of an angle in degrees.

  Args:
    angle_degrees: The angle in degrees.

  Returns:
    A tuple containing the sine, cosine, and tangent values.
    Returns None if the tangent is undefined (angle is an odd multiple of 90 degrees).
  """
  angle_radians = math.radians(angle_degrees)

  sin_value = math.sin(angle_radians)
  cos_value = math.cos(angle_radians)

  # Check for undefined tangent (tan(90), tan(270), etc.)
  if cos_value == 0:
    return None  # Tangent is undefined

  tan_value = math.tan(angle_radians)

  return sin_value, cos_value, tan_value

# Example usage:
angle = 45
results = calculate_trigonometric_values(angle)

if results:
  sin_result, cos_result, tan_result = results
  print(f"For angle {angle} degrees:")
  print(f"  Sine: {sin_result}")
  print(f"  Cosine: {cos_result}")
  print(f"  Tangent: {tan_result}")
else:
  print(f"Tangent for angle {angle} degrees is undefined.")

angle2 = 90
results2 = calculate_trigonometric_values(angle2)

if results2:
    sin_result2, cos_result2, tan_result2 = results2
    print(f"For angle {angle2} degrees:")
    print(f"  Sine: {sin_result2}")
    print(f"  Cosine: {cos_result2}")
    print(f"  Tangent: {tan_result2}")
else:
    print(f"Tangent for angle {angle2} degrees is undefined.")

angle3 = 30
results3 = calculate_trigonometric_values(angle3)

if results3:
    sin_result3, cos_result3, tan_result3 = results3
    print(f"For angle {angle3} degrees:")
    print(f"  Sine: {sin_result3}")
    print(f"  Cosine: {cos_result3}")
    print(f"  Tangent: {tan_result3}")
else:
    print(f"Tangent for angle {angle3} degrees is undefined.")