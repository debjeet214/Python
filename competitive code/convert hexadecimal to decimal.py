hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    hexNum = hexNum.upper()  # Ensure the input is in uppercase to match the dictionary keys
    decimal_value = 0
    
    for i, char in enumerate(reversed(hexNum)):
        if char in hexNumbers:
            decimal_value += hexNumbers[char] * (16 ** i)
        else:
            return None  # Return None if the character is not a valid hexadecimal digit
    
    return decimal_value

# Example usage:
print(hexToDec('1A3'))  # Output: 419
print(hexToDec('G1'))   # Output: None
