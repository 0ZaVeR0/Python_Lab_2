def create_mask(offset):
    b_mask = 0b11111111_11111111_11111111_11111111 - offset
    b_mask = bin(b_mask)[2:].zfill(32)

    str_mask_1 = str(int(b_mask[0:8],2)).zfill(3)
    str_mask_2 = str(int(b_mask[8:16],2)).zfill(3)
    str_mask_3 = str(int(b_mask[16:24],2)).zfill(3)
    str_mask_4 = str(int(b_mask[24:32],2)).zfill(3)

    mask = str_mask_1 + "." + str_mask_2 + \
        "." + str_mask_3 + "." + str_mask_4 + "\n"
    return mask

file = open("mask.log","w")
b_offset = 0b0

file.write(create_mask(b_offset))
while b_offset != 0b11111111_11111111_11111111_11111111:
    b_offset = b_offset << 1
    b_offset = b_offset | 0b1
    file.write(create_mask(b_offset))

file.close()