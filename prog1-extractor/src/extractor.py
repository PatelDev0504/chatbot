companyName = ""
filename = ""
print("Enter 1 to load the data of NVIDIA")
print("Enter 2 to load the data of AMD")
keyboard = input("Please input now:")
if (keyboard == "1"):
    filename = 'NVIDIA_1-29-23.txt'
    companyName = "NVIDIA"
elif (keyboard == "2"):
    filename = 'AMD_12-30-23.txt'
    companyName = "AMD"
num_of_words = 0
num_of_lines = 0
num_of_chars = 0
num_of_parts = 0
parts = []
with open('CSCE240_chat_bot/prog1-extractor/data/'+filename, "r") as f:
    for line in f:
        if (line.__contains__("PART ")):
            parts.append(line)
        words = line.split(" ")
        num_of_chars += len(line)
        num_of_lines += 1
        num_of_words += len(words)
f.close()



with open("CSCE240_chat_bot/prog1-extractor/data/output.txt", "a") as f:
    f.write(companyName)
    f.write("\n\tNumber of words in the file: " + str(num_of_words))
    f.write("\n\tNumber of lines in the file: " + str(num_of_lines))
    f.write("\n\tNumber of characters in the file: " + str(num_of_chars))
    f.write("\n\tNumber of parts in the file: " + str(len(set(parts)))+"\n")
f.close()
