#!/usr/bin/python3
"""
UTF-8 Validation Script
"""

def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.

    Args:
    - data (list): A list of integers representing 1-byte data.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else False.
    """
    i = 0
    while i < len(data):
        byte = data[i]

        if byte & 0x80 == 0:  # Single-byte character
            i += 1
        else:
            length = determine_length(byte)
            if not validate_remaining_bytes(data, i + 1, length):
                return False
            i += length

    return True

def determine_length(byte):
    """
    Determine the length of the character based on the number of leading '1' bits.

    Args:
    - byte (int): The byte to analyze.

    Returns:
    - int: The length of the character.
    """
    length = 0
    mask = 0x80
    while (byte & mask) != 0:
        length += 1
        mask >>= 1

    return max(1, length)  # Minimum length is 1

def validate_remaining_bytes(data, start, length):
    """
    Validate the remaining bytes in the multi-byte sequence.

    Args:
    - data (list): A list of integers representing 1-byte data.
    - start (int): The starting index of the multi-byte sequence.
    - length (int): The length of the multi-byte sequence.

    Returns:
    - bool: True if the remaining bytes are valid, else False.
    """
    for i in range(start + 1, start + length):
        if i >= len(data) or (data[i] & 0xC0) != 0x80:
            return False

    return True

if __name__ == "__main__":
    # Test the function
    data_set = [197, 130, 1]  # Example UTF-8 encoded data set
    result = validUTF8(data_set)
    print(result)

