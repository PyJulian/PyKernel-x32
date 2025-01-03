#import <python.h>
#import "kernel_py.h"

terminal_buffer = (uint16_t*) 0xC03FF000;

void kernel_main {
    Py_Initialize();
    Py_Finalize();
    while (1);
}
