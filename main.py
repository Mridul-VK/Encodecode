english_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findArr(array, value):
  for index, item in enumerate(array):
    if item == value:
      return index
    else:
      continue


def encode(inp_txt, eng_char):
  out_txt_arr = []
  for index, char in enumerate(inp_txt):
    char = char.lower()
    if(char not in eng_char):
      out_txt_arr.append(char)
    else:
      try:
        char_index = findArr(eng_char, char)
        if index % 4 == 1 :
          out_txt_arr.append(eng_char[char_index-7])
        elif index % 4 == 2 :
          if char_index + 1 > 25:
            char_index -= 26
          out_txt_arr.append(eng_char[char_index+1])
        elif index % 4 == 3 :
          out_txt_arr.append(eng_char[char_index])
        elif index % 4 == 0:
          if char_index + 4 > 25:
            char_index -= 26
          out_txt_arr.append(eng_char[char_index+4])
      except Exception as e:
        print(e)

  return out_txt_arr

  
def decode(inp_txt, eng_char):
  out_txt_arr = []
  for index, char in enumerate(inp_txt):
    char = char.lower()
    if(char not in eng_char):
      out_txt_arr.append(char)
    else:
      try:
        char_index = findArr(eng_char, char)
        if index % 4 == 1 :
          if char_index + 7 > 25:
            char_index -= 26
          out_txt_arr.append(eng_char[char_index+7])
        elif index % 4 == 2 :
          out_txt_arr.append(eng_char[char_index-1])
        elif index % 4 == 3 :
          out_txt_arr.append(eng_char[char_index])
        elif index % 4 == 0:
          out_txt_arr.append(eng_char[char_index-4])
      except Exception as e:
        print(e)

  return out_txt_arr

def user_input(user_name):
  action_type = input(f"So {user_name}, Which operation would you like me to handle now? (enc/dec): ")
  print("--------------------------------------------")

  match action_type:
    case "enc":
      input_text = input(f"Ohkay {user_name}! Enter message to be encoded: ")
      output_text_array = encode(input_text, english_chars)
      output_text = ''.join(output_text_array)
      print("--------------------------------------------")
      print("ENCODED: " + output_text)
      print("--------------------------------------------")
    case "dec":
      input_text = input(f"Ohkay {user_name}! Enter message to be decoded: ")
      output_text_array = decode(input_text, english_chars)
      output_text = ''.join(output_text_array)
      print("--------------------------------------------")
      print("DECODED: " + output_text)
      print("--------------------------------------------")
    case _:
      print("--------------------------------------------")
      print(f"Sorry {user_name}, your input is not valid!")
      print("--------------------------------------------")
      
  yes_no = input(f"Would you like to reuse {user_name}? (Y/N): ")
  if yes_no.lower() == 'y':
    print("--------------------------------------------")
    user_input(user_name)
  elif yes_no.lower() == 'n':
    print("--------------------------------------------")
    print(f"Ohkay {user_name}, I hope you enjoyed 😉. Hope to see you again. 👋 Bye {user_name}")
    print("--------------------------------------------")
  else:
    print("--------------------------------------------")
    print(f"Well I didn't get what you meant but I pressume you said no. I hope you enjoyed 😉. Hope to see you again. 👋 Bye {user_name}")
    print("--------------------------------------------")
  


print("--------------------------------------------")
name = input("Enter your name please 😇: ")
print("--------------------------------------------")
print(f"👋 Hello {name}, I'm Encodecode Wizard. I'll help you talk to your friend secretly 😜")
print("--------------------------------------------")

user_input(name)
