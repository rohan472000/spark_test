def append_lines_function(lines):
    output_lines = []
    current_line = ''
    for line in lines:
        line_parts = line.strip().split('|')
        # print('line parts 1 :', line_parts) check for correct line strip
        if line_parts[0].strip() == line_parts[1].strip().split()[0]:  # check  len(line_parts) > 1 if line has only one element
            # print('line parts',line_parts)
            # print(line_parts[1].strip().split()[0]) to remove spaces after first '|'
            output_lines.append(line.strip())
            current_line = ''
        else:
            current_line += line.strip() #+ ' '
            # print(current_line)
            if current_line.strip():
                output_lines[-1] = output_lines[-1] + current_line.strip()   # add this +' ' if space is required
    return output_lines


with open("input.txt") as f:
    lines = f.readlines()
    appended_lines = append_lines_function(lines)

with open("output.txt", "w") as f:
    for line in appended_lines:
        f.write(line + "\n")
