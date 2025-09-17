def encode(message, shift):
    # Encodes a message by shifting the message using the shift value
    encoded = []
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            # Performing the shift operation for encoding and decoding
            encoded.append(encoded_char)
        else:
            encoded.append(char)
    return ''.join(encoded)

def decode(message, shift):
    # Decodes a message by shifting the message using the shift value
    return encode(message, -shift)

def menu():
    print("\nSecret Code Generator")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == '1':
            message = input("Enter the message to encode: ")
            shift = int(input("Enter the shift number: "))
            encoded = encode(message, shift)
            print(f"Encoded message: {encoded}")
        elif choice == '2':
            message = input("Enter the message to decode: ")
            shift = int(input("Enter the shift number: "))
            decoded = decode(message, shift)
            print(f"Decoded message: {decoded}")
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
