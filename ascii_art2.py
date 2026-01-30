ASCII_CHARS = " .:-=+*#%@"

def read_ppm_p3(filename):
    with open(filename, "r") as f:
        data = f.read().split()

    if data[0] != "P3":
        raise ValueError("Invalid PPM format")

    width = int(data[1])
    height = int(data[2])

    pixels = list(map(int, data[4:]))

    image = []
    idx = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            r = pixels[idx]
            g = pixels[idx + 1]
            b = pixels[idx + 2]
            idx += 3
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            row.append(gray)
        image.append(row)

    return image


def normalize(image):
    flat = [px for row in image for px in row]
    mn, mx = min(flat), max(flat)

    norm = []
    for row in image:
        norm_row = []
        for px in row:
            val = int((px - mn) * 255 / (mx - mn))
            norm_row.append(val)
        norm.append(norm_row)

    return norm


def to_ascii(image):
    h = len(image)
    w = len(image[0])
    scale = len(ASCII_CHARS) - 1

    ascii_img = []

    for i in range(0, h - 1, 2):
        line = ""
        for j in range(0, w - 1, 2):
            avg = (
                image[i][j] +
                image[i][j + 1] +
                image[i + 1][j] +
                image[i + 1][j + 1]
            ) // 4
            line += ASCII_CHARS[avg * scale // 255]
        ascii_img.append(line)

    return ascii_img


image = read_ppm_p3("allu_arjun_p3.ppm")
image = normalize(image)
ascii_image = to_ascii(image)

with open("ascii_output2.txt", "w") as f:
    for line in ascii_image:
        f.write(line + "\n")

print("ASCII art generated successfully")
