def encode(password):
    encoded_password = ''
    for char in password:
        new_char = chr(ord(char) + 3)
        encoded_password += new_char
    return encoded_password

def decode(encoded_password):
    decoded_password = ''
    for char in encoded_password:
        original_char = chr(ord(char) - 3)
        decoded_password += original_char
    return decoded_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "
        if option == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == 3:
            break

if __name__ == "__main__":
    main()
