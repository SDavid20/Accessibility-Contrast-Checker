def hex_to_rgb(hex_color):
    # Functions converts the 6 digit hex colour code to it's RGB component
    hex_color = hex_color.lstrip('#')  # Remove the "#" tag in the instance that a user to the inputed hex code
    # Convert the hex code to RGB
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))  # used a tuple to make the date immutable


def relative_luminance(rgb):
    # function normalise the RGB values to a range between 0 to 1
    r, g, b = [x / 255.0 for x in rgb]

    # Apply luminance transformation
    # Method is given by World Wide Web Consortium
    # For value <= 0.03928 use simple division
    # For value > 0.0392 use complex method.
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

    # Calculate relative luminance
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(l1, l2):
    # Functions makes sure l1 has a higher luminance than l2
    l1, l2 = max(l1, l2), min(l1, l2)
    return (l1 + 0.05) / (l2 + 0.05)


def contrast_checker(contrast):
    # Function determine the level of accessibility based on the contrast ratio defined by w3c
    if contrast >= 7:
        return "AAA (sufficient for all text)"
    elif contrast >= 4.5:
        return "AA (sufficient for normal text)"
    elif contrast >= 3:
        return "AA Large (sufficient for large text)"
    else:
        return "Fail (insufficient contrast)"


def is_valid_hex_code(hex_color):
    # Function to check if a given hex color code is valid
    hex_color = hex_color.lstrip('#')
    return len(hex_color) == 6 and all(c in '0123456789ABCDEFabcdef' for c in hex_color)

def get_valid_hex_input(prompt):
    while True:
        color = input(prompt)
        if is_valid_hex_code(color):
            return color
        else:
            print("Invalid hex color code. Please enter a valid 6-digit hex code (e.g., #FFFFFF).")

def main():
    # Get valid hex color codes
    foreground_color = get_valid_hex_input("Enter the hex code of your foreground (e.g., #FFFFFF): ")
    background_color = get_valid_hex_input("Enter the hex code of your background (e.g., #FFFFFF): ") 

    # Convert hex to rgb component
    foreground_rgb = hex_to_rgb(foreground_color)
    background_rgb = hex_to_rgb(background_color)

    # Calculate Relative Luminance
    foreground_luminance = relative_luminance(foreground_rgb)
    background_luminance = relative_luminance(background_rgb)

    # Calculate contrast ratio
    ratio = contrast_ratio(foreground_luminance, background_luminance)

    result = contrast_checker(ratio)

    print(f"Contrast ratio: {ratio:.2f}")
    print(f"Accessibility level: {result}")


if __name__ == "__main__":
    main()
