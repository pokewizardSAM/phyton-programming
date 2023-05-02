def calculate(filesize):    
    blocks_int = filesize//4096
    blocks_float = filesize/4096
    if blocks_int*4096 == blocks_float*4096:
        print(blocks_int*4096)
    else:
        print((blocks_int+1)*4096)

calculate(6000)