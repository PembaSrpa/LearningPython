# # your text message here:
# text = "Lost From Light!"

# import time

# current_text = ""

# print(end='\x1b[?25l', flush=True)

# while current_text != text:
#     for char in map(chr, range(32, 127)):
#         print(current_text + char)
#         time.sleep(0.01)

#         if char == text[len(current_text)]:
#             current_text += char
#             break

#     else:
#         current_text += text[len(current_text)]
#         print(current_text)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import time

# text = "Fok You!"
# current_text = ""

# while current_text != text:
#     for char in (chr(i) for i in range(32, 127)):
#         print(current_text + char)
#         time.sleep(0.01)

#         if char == text[len(current_text)]:
#             current_text += char
#             break
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import time

text = "Duck You!"
current_text = [""] * len(text)  # Empty placeholders
index = len(text) - 1            # Start from the end

while index >= 0:
    for char in (chr(i) for i in range(32, 127)):
        current_text[index] = char
        print("".join(current_text))
        time.sleep(0.01)

        if char == text[index]:
            break
    index -= 1
