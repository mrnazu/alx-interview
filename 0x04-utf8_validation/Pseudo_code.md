function validUTF8(data):
    for byte in data:
        if byte is a single-byte character:
            continue
        else:
            length = determine_length(byte)
            
            if not validate_remaining_bytes(data, length):
                return False
    
    return True

