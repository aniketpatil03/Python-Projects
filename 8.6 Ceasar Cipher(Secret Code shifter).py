# this is seperate method approach
#---------------------------------------------------------------------------------
# Double list of alphabets will ensure shift is continued for last alphabets also

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# def encrypt(plain_text,shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"the encrypted msg text is {cipher_text}")
#
# def decrypt(coded_text,shift_amount):
#     plain_text = ""
#     for letter in coded_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decrypted text is :{plain_text}")
#
# display_msg = input("Encrpt or Decrypt")
# if display_msg.lower() == "encrypt":
#     text = input("Enter text ")
#     shift = int(input("Enter shift number "))
#     encrypt(plain_text=text,shift_amount=shift)
# else:
#     text = input("Enter text to decode: ")
#     shift = int(input("Enter shift value: "))
#     decrypt(coded_text=text,shift_amount=shift)
# ------------------------------------------------------------------------------------
# Combined both decode and encode function approach
#------------------------------------------------------------------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# below are common to both encrypt and decrypt ,  hence taken for both together
direction = input("Encode or Decode: \n")
text = input("Enter text\n").lower()
shift = int(input("Shift no: "))


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"the {direction}d msg is {end_text}")


ceasar(text, shift, direction)
