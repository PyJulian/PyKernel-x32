def kernel_main():
    terminal_buffer = 0xC03FF000
    message = "Hello, kernel!"
    for i, char in enumerate(message):
        memory_address = terminal_buffer + (i * 2)
        set_memory(memory_address, ord(char), 0x07)


def set_memory(address, char, color):
    pass
