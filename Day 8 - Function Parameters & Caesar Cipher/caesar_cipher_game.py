alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]  #alphabet list


def caesar(start_text, shift_amount,
           cipher_direction):  #function for caesar cipher
    end_text = ""  #empty string
    if cipher_direction == "decode":  #if decode is selected
        shift_amount *= -1  #shift amount is multiplied by -1
    for char in start_text:  #for loop for each character in the text
        if char in alphabet:  #if the character is in the alphabet
            position = alphabet.index(
                char)  #position is the index of the character in the alphabet
            new_position = position + shift_amount  #new position is the position plus the shift amount
            end_text += alphabet[
                new_position]  #end text is the alphabet at the new position
        else:  #else
            end_text += char  #end text is the character
    print(f"Here's the {cipher_direction}d result: {end_text}"
          )  #prints the result


from art import logo  #import logo from art.py

print(logo)  #prints logo

should_end = False  #should end is false
while not should_end:  #while should end is false

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"
                      )  #direction is the input of the user
    text = input(
        "Type your message:\n").lower()  #text is the input of the user
    shift = int(
        input("Type the shift number:\n"))  #shift is the input of the user
    shift = shift % 26  #shift is the shift amount mod 26
    caesar(start_text=text, shift_amount=shift,
           cipher_direction=direction)  #calls the caesar function

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    )  #restart is the input of the user
    if restart == "no":  #if restart is no
        should_end = True  #should end is true
        print("Goodbye")  #prints goodbye
