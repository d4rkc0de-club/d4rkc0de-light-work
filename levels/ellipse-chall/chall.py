import math
import random

# Flag to encode (can be modified later)
flag = "d0rk{REDACTED}c0de"
flag_bytes = [ord(c) for c in flag]  # convert each character to ASCII

# Ellipse parameters (large enough to span ASCII range)
a = 30
b = 20

# Function to compute y from x and theta
def compute_y(m, x):
    sqrt_term = math.sqrt(a**2 * m**2 + b**2)
    return m * x + sqrt_term  # using +sqrt branch

# Store the results
output_data = []

for byte in flag_bytes:
    # Pick a random theta within a safe range to avoid extreme slopes
    theta = random.uniform(-math.pi / 3, math.pi / 3)
    m = math.tan(theta)
    x = float(byte)  # treat the ASCII code as x
    y = compute_y(m, x)

    # Round for cleaner output
    output_data.append((round(y, 5), round(theta, 5)))


# Write to output file
with open("output.txt", "w") as f:
    for y, theta in output_data:
        f.write(f"{y},{theta}\n")
