def create_ip(ip):
    
    str_mask_1 = str(int(ip[0:8],2)).zfill(3)
    str_mask_2 = str(int(ip[8:16],2)).zfill(3)
    str_mask_3 = str(int(ip[16:24],2)).zfill(3)
    str_mask_4 = str(int(ip[24:32],2)).zfill(3)

    ip = str_mask_1 + "." + str_mask_2 + \
        "." + str_mask_3 + "." + str_mask_4 + "\n"
    return ip

def to_binary(str_mask):
    arr_mask = list(str_mask.split("."))
    str_mask = str()

    for i in range(len(arr_mask)):
        str_mask += str(bin(int(arr_mask[i])))[2:].zfill(8)
    
    return str_mask

file_mask = open("mask.log","r")
file_ip = open("ip_solve.log","w")

str_ip = to_binary(input())

for i in range(33):
    str_mask = to_binary(file_mask.readline())
    int_ones = str_mask.count("1")

    net_adress = str_ip[:int_ones] + str_mask [int_ones:33]

    file_ip.write(create_ip(net_adress))

file_mask.close()
file_ip.close()