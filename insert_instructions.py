def insert_instructions(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if 'callq' in line:
            new_lines.append(line)
            new_lines.append('    prefetchnta 0x11223344\n')  # Add prefetcha after each callq
        elif 'retq' in line:
            new_lines.append('    jmp cfi_check_ret\n')  # Replace retq with jmp
        else:
            new_lines.append(line)

    with open(filename, 'w') as file:
        file.writelines(new_lines)

insert_instructions('CADET.s')

