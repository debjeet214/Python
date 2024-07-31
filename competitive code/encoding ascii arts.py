def encode_ascii_art(ascii_art):
    lines = ascii_art.split('\n')
    encoded_lines = []
    for line in lines:
        encoded_line = ','.join(str(ord(char)) for char in line)
        encoded_lines.append(encoded_line)
    encoded_art = '\n'.join(encoded_lines)
    return encoded_art

def decode_ascii_art(encoded_art):
    encoded_lines = encoded_art.split('\n')
    decoded_lines = []
    for encoded_line in encoded_lines:
        decoded_line = ''.join(chr(int(value)) for value in encoded_line.split(','))
        decoded_lines.append(decoded_line)
    decoded_art = '\n'.join(decoded_lines)
    return decoded_art

# Example ASCII art
ascii_art = """
:-)
;-)
:-(
"""

# Encode the ASCII art
encoded_art = encode_ascii_art(ascii_art.strip())
print("Encoded ASCII Art:\n", encoded_art)

# Decode the encoded ASCII art
decoded_art = decode_ascii_art(encoded_art)
print("\nDecoded ASCII Art:\n", decoded_art)
