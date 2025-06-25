try:
    with open('sample.txt', 'r') as file1:
        read_line1 = file1.readline()
        read_line2 = file1.readline()
        read_line3 = file1.readline()
        
        print("Reading file content:")
        print("Line 1:", read_line1.strip())
        print("Line 2:", read_line2.strip())
        print("Line 3:", read_line3.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")



