def read_file(file_path):
    """Reads a text file and returns a set of lines."""
    with open(file_path, 'r') as file:
        return set(file.readlines())

def main():
    file1 = 'text_1.txt'
    file2 = 'text_2.txt'
    
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)
    
    differences = file2_lines - file1_lines
    
    if differences:
        print("Rows in text_2.txt but not in text_1.txt:")
        for line in differences:
            print(line.strip())
    else:
        print("No differences found. Both files have the same data.")

if __name__ == "__main__":
    main()
