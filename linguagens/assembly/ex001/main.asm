.global _start
.intel_syntax noprefix

# para rodar: crtl+shift+p -> Run Task -> Assembly: exec

_start: # equivalente ao main
    CALL print_hello_world 
    JMP exit

print_hello_world:  # função para escrever na tela 
    MOV rdi, 0x01
    LEA rsi, [hello_str]
    MOV rdx, 14
    SYSCALL
    RET

exit: # encerra o processo
    MOV rax, 0x3c
    MOV rdi, 0 
    SYSCALL


.section .data
    hello_str: .asciz "hello, world!\n"


