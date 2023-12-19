alphabet = "abcdefghijklmnopqrstuvwxyz"

#message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"



#translated_message = ""

#for character in message:
  #if character in alphabet:
    #character_value = alphabet.find(character)
   # translated_message += alphabet[(character_value + 10) % 26]
  #else:
   # translated_message += character

#print(translated_message)
#message = "hi there vishal i hope stuff is well and all and all is well"

#new message sent from Vishal
new_message = " jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

#func for decoding Ceaser Cypher
def ceaser_decode(message, offset):
    translated_message = ""
    for character in new_message:
        if character in alphabet:
            first_character_value = alphabet.find(character)
            translated_message += alphabet[(first_character_value + offset) % 26]
        else:
            translated_message += character
    return translated_message

first_decoded_message = ceaser_decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.",10)
print(first_decoded_message)


#func for decoding Ceaser Cypher
def second_ceaser_decode(message, offset):
    translated_second_message = ""
    for character in message:  
        if character in alphabet:
            second_character_value = alphabet.find(character)
            translated_second_message += alphabet[(second_character_value + offset) % 26]
        else:
            translated_second_message += character
    return translated_second_message 

decoded_message = second_ceaser_decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)
print(decoded_message)

def Vigenère_cipher(message,keyword):
    broken_cipher = []
    for character in message:
        mes
        for letters in keyword:

        if character in alphabet:
            shifted_character = alphabet.find(character)

