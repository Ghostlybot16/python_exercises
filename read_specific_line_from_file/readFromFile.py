def read_line(fname, lnum):
    
    try:
        # open the file in reading mode 
        file = open(fname, "r")

        lines = file.readlines() # read file lines. This returns as a list
        file.close() 
    except:
        print("Error reading file.")
        return 

    total_lines = len(lines)

    if(lnum > total_lines):
            print(str(total_lines) + " file lines.")
            print("Can't read line " + str(lnum) + "!")
    else:
        line = lines[lnum - 1].rstrip('\n')
        print(line)

filename = input("File: ")
line_number = int(input("Line: "))

read_line(filename, line_number)
