raw_binary_report = 'binary_report.txt'
csv_binary_report = 'binary_report.csv'
input_file  = open(raw_binary_report, 'r')
output_file = open(csv_binary_report, 'w+')

file_content = input_file.readlines()
print(len(file_content))

for line in file_content:
    output_array = []
    for char in str(line):
        output_array.append(char)
    output_line = ','.join(output_array)
    output_file.write(output_line)

input_file.close()
output_file.close()
