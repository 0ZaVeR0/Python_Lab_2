file_input = open ("article.txt","r",encoding="utf8")

text = file_input.readlines()
data_dict = {}
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
for line in text:
    line = line.lower()

    for x in line:
        if x in alphabet:
            try: 
                data_dict[x] += 1
            except KeyError:
                data_dict[x] = 1 
file_input.close()

all_char = sum(data_dict.values())
data_dict = dict(reversed(sorted(data_dict.items(), key=lambda item: item[1])))

for x in data_dict:
    data_dict.update({x:data_dict[x] / all_char})

file_output  = open ("article_solve.txt","w",encoding="utf8")
for x in data_dict:
    file_output.write(x + ": " + str(data_dict[x]) + "\n")
file_output.close()