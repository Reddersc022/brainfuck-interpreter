![licence](https://img.shields.io/github/license/reddersc022/brainfuck-interpreter)

# Brainfuck Interpreter  
Enclosed is an interpreter, written in Python currently, to run [BrainFuck](https://en.wikipedia.org/wiki/Brainfuck) code.

### Syntax
- `>` : Increment pointer
- `<` : Decrement pointer
- `+` : Increment data at pointer
- `-` : Decrement data at pointer
- `.` : Output integer at pointer
- `,` : Save one integer of input to pointer
- `[` : If integer at pointer is 0, jump to after matching `]`, continue otherwise
- `]` : If integer at pointer is non-0, jump to starting `[`, continue otherwise
- `#` : Comment, anything afterward will be ignored (until newline)

### Rules
- All values stored are initially 0, and can only be integers.  
- The array of values has a constant length (usually 30,000) and this can be edited in the code. Any attempt to access past the max length will result in an error.  
- Any inputs must be either:  
    - An integer or single character in the Python version
    - A single character in the C version  
    Anything else throws an error

### Usage
#### Python
``python src\brainfuck.py code_file.bf``
#### C
``gcc -o brainfuck src/brainfuck.c``  
``brainfuck code_file.bf``

### Tests
#### Python
To add two inputted numbers:  
``python src\brainfuck.py tests\add_two_numbers.bf``  
To echo any input:  
``python src\brainfuck.py tests\echo.bf``  
Hello world!  
``python src\brainfuck.py tests\hello_world.bf``  
#### C
To add two inputted numbers:  
``brainfuck tests\add_two_numbers.bf``  
To echo any input:  
``brainfuck tests\echo.bf``  
Hello world!  
``brainfuck tests\hello_world.bf``  

### Notes
- The end state will be saved as: ``outputs\end_states\dd-mm-yy hhmmss.json``
- Any output will be saved as: ``outputs\output\dd-mm-yy hhmmss.txt``

### TODO
#### Python:
- [x] Implement basic syntax  
- [x] Implement comments  
#### C:
- [x] Implement basic syntax  
- [x] Implement comments  