# Arnav Bagmar

def encode(password):
    encoded_password = ''
    for char in password:
        encoded_digit = (int(char) + 3) % 10  # Shift the digit by 3 positions (mod 10 to handle wraparound)
        encoded_password += str(encoded_digit)
    return encoded_password

def decode(password):
    encoded_password = ''
    for char in password:
        encoded_digit = (int(char) - 3) % 10  # Shift the digit by 3 positions (mod 10 to handle wraparound)
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
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
