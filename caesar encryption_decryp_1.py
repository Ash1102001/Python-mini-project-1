alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
          'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

def caeser(message, shift_amount, task):
    new_text = ""
    for char in message :
      if char in alphabet:
        position = alphabet.index(char)
        if task == "encode":
          new_pos = position + shift_amount
        elif task == "decode":
          new_pos = position - shift_amount   
        new_text += alphabet[new_pos]
      else:
          new_text += char
    print(f"Here is the {direction}d result: {new_text}")


caeser(message = text, shift_amount = shift, task = direction)
    

