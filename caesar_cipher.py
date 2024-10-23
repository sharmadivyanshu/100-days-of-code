import string
import re


alphabets = list(string.ascii_letters)

def encrypt_or_decrypt(text: str, shift: int, reverse=False) -> str:
    total_alphabets = len(alphabets)
    resulted_text = ""
    for letter in text:
        if re.search(r"[^a-zA-Z]", letter):
            resulted_text += letter
            continue
        if reverse:
            shifted_position = alphabets.index(letter) - shift
        else:
            shifted_position = alphabets.index(letter) + shift
        shifted_position %= total_alphabets
        resulted_text += alphabets[shifted_position]
    return resulted_text


if __name__ == "__main__":
    run_again = True
    while run_again:
        print("\nWhat do you want to do?\n")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("--> ").lower()
        if choice not in ["encrypt", "decrypt", "1", "2"]:
            print("Please select valid choice from the options")
            continue
        letter_shift = int(input("\nEnter the shift value: "))
        message = input("\nEnter the message: ")
        result = encrypt_or_decrypt(message, letter_shift) if choice in ["encrypt", "1"] else encrypt_or_decrypt(message, letter_shift, True)
        print(f"Message: {result}")
        run_again = input("\nDo you want to go again? ")
        run_again = run_again in ["yes", "y"]

