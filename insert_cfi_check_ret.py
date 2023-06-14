def insert_cfi_check_ret(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    cfi_check_ret = """
.globl cfi_check_ret
.type cfi_check_ret, @function
cfi_check_ret:
    push %rax
    movq 8(%rsp), %rax
    cmpl $0x11223344, 4(%rax)
    jne .L_failed_ret
    pop %rax
    retq
.L_failed_ret:
    call exit
"""
    # Insert cfi_check_ret at the beginning of the file
    lines.insert(0, cfi_check_ret)

    with open(filename, 'w') as file:
        file.writelines(lines)

insert_cfi_check_ret('CADET_test1.s')

