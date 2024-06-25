# Read and modify the first file
with open('file1.txt', 'r') as file1:
    file1_lines = file1.readlines()
    modified_lines = [line.strip() + "='" for line in file1_lines]

# Read the second file
with open('file2.txt', 'r') as file2:
    file2_lines = file2.readlines()
    final_lines = [line.strip() + "'" for line in file2_lines]

# Combine the modified lines
combined_lines = modified_lines + final_lines

# Write the combined lines to a new file (or overwrite an existing file)
with open('output.txt', 'w') as output_file:
    for line in combined_lines:
        output_file.write(line + "\n")

print("Processing complete. Check 'output.txt' for the result.")
