import csv

with open("store.csv",'r',encoding= "utf8") as file_input:
    csv_reader = csv.reader(file_input)
    headers = next(csv_reader)
    data_dict = {}
    for row in csv_reader:
        try: 
            data_dict[row[1]] += float(row[2])
        except KeyError:
            data_dict[row[1]] = float(row[2]) 
file_input.close()

with open("categories.csv",'w',encoding= "utf8",newline='') as file_output:
    csv_writer = csv.writer(file_output)
    fields = ["Категория","Стоимость"]
    csv_writer.writerow(fields)
    dict_keys = data_dict.keys()
    for x in dict_keys:
        csv_writer.writerow([x,data_dict[x]])
file_output.close()