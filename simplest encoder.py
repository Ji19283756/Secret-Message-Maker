def encode(message,letters,encoded_word = []):
    def string_to_numbers(message):
        return [letters_dict_encode[letter] for letter in message]
    letters_dict_encode={letter:x+1 for x,letter in enumerate(letters)}
    message=list(message)
    message=string_to_numbers(message)
    current = message[0]    #sets the current word to the firs word
    encoded_word += [message[0]] #adds the current word to the message
    message.pop(0)
    for x in range(1, len(message) + 1):
        #if x % 2 == 0:  # moves to the left
        #    if current > message[0]:  # if the next letter before the current
        #        encoded_word += [current - message[0]]
        #    else:  # if the next letter comes after the current
        #        encoded_word += [len(letters_dict_encode)  - (message[0] - current)]
        #else:  # moves to the right
        #    if message[0] > current:  # if the next letter comes after the current
        #        encoded_word += [message[0] - current]
        #    else:  # if the next letter comes before the current
        #        encoded_word += [len(letters_dict_encode)  - (current - message[0])]
        encoded_word += [  # does all of this^^^^, but branchless , so yeah idk
            ((x % 2 == 0 and current > message[0]) * (current - message[0]) +
             ((x % 2 == 0 and not current > message[0]) *
              (len(letters_dict_encode) - (message[0] - current))) +
             ((x % 2 == 1 and message[0] > current) * (message[0] - current)) +
             ((x % 2 == 1 and not message[0] > current) *
              (len(letters_dict_encode) - (current - message[0]))))]
        current = message[0]
        message.pop(0)
    return encoded_word

def decode(message_array,letters):
    letters_dict_decode = {x + 1: letter for x, letter in enumerate(letters)}
    return_decoded_string = ""
    current = message_array[0]
    return_decoded_string += letters_dict_decode[message_array[0]]
    message_array.pop(0)
    for x in range(1, len(message_array) + 1):
        if x % 2 == 0:  # moves to the left
            current = current - message_array[0]
        else:  # moves to the right
            current = (current + message_array[0]) % len(letters_dict_decode)
        current += ((current <= 0) * len(letters_dict_decode))  # executes in case current is below or equal to 0
        return_decoded_string += letters_dict_decode[current]
        message_array.pop(0)
    return return_decoded_string


#OPTIONS:________________________________________________________________________________________

letters = "abcdefghijklmnopqrstuvwxyz "

message="because"

#________________________________________________________________________________________________

encoded_message=encode(message,letters)

print(encoded_message)

decoded_message=decode(encoded_message,letters)

print(decoded_message)

#[2, 3, 2, 25, 7, 25, 14]