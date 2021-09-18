"""Main runfile for interpreting BrianFuck code"""

import json
import time
from typing import List

ARRAY_SIZE = 30_000


def sort_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        content = f.read().replace(" ", "").split("\n")
    
    code = ""
    for line in content:
        for char in line:
            if char == "#":
                break
            else:
                code += char
    
    return code


def save_end_state(state: List[int], dir: str = "outputs\end_states"):
    date_time = time.strftime("%d-%m-%y %H%M%S")
    file_name = f"{dir}\\{date_time}.json"
    with open(file_name, "w") as f:
        json.dump(state, f)
    print(f"End state saved at {file_name}")


def add_to_output(value: int, file: str):
    with open(file, "a") as f:
        f.write(chr(value))


def sort_error(ins_pointer: int, message: str):
    print(f"** Error at character {ins_pointer}:")
    print(message)


def main(args: List[str]):
    if len(args) != 2:
        print("Please provide one file to use (ie., python src\\brainfuck.py tests\\echo)")
        return
    
    file = args[1]
    code = sort_file(file)

    array = [0 for _ in range(ARRAY_SIZE)]
    array_pointer = 0

    instruction_pointer = 0

    in_loop = False
    loop_stack = []

    out_file = f"outputs\output\{time.strftime('%d-%m-%y %H%M%S')}.txt"

    while instruction_pointer < len(code):
        instruction = code[instruction_pointer]

        # Sort instruction
        if instruction == ">":
            if array_pointer < ARRAY_SIZE - 1:
                array_pointer += 1
            else:
                sort_error(
                    instruction_pointer,
                    f"Array pointer should not be greater than array length ({ARRAY_SIZE})"
                )
                break
        elif instruction == "<":
            if array_pointer > 0:
                array_pointer -= 1
            else:
                sort_error(
                    instruction_pointer,
                    "Array pointer should not be less than 0"
                )
                break
        elif instruction == "+":
            array[array_pointer] += 1
        elif instruction == "-":
            array[array_pointer] -= 1
        elif instruction == ".":
            print(f"Output: {chr(array[array_pointer])} (int: {array[array_pointer]})")
            add_to_output(array[array_pointer], out_file)
        elif instruction == ",":
            inp = input("Input: ")
            if inp.isdigit():
                array[array_pointer] = int(inp)
            elif len(inp) != 1:
                sort_error(
                    instruction_pointer,
                    f"Input should be either an integer or single character (not {inp})"
                )
                break
            else:
                array[array_pointer] = ord(inp)
        elif instruction == "[":
            if array[array_pointer] == 0:
                depth = 0
                while depth >= 0:
                    instruction_pointer += 1
                    instruction = code[instruction_pointer]
                    if instruction == "[":
                        depth += 1
                    elif instruction == "]":
                        depth -= 1
            else:
                in_loop = True
                loop_stack.append(instruction_pointer)
        elif instruction == "]":
            if not in_loop:
                sort_error(
                    instruction_pointer,
                    f"`]` found when not in loop (no matching `[`)"
                )
                break
            elif array[array_pointer] == 0:
                loop_stack.pop(-1)
            else:
                instruction_pointer = loop_stack[-1]

        # Finish up
        instruction_pointer += 1
    save_end_state(array)
    return


if __name__ == "__main__":
    import sys
    args = sys.argv
    main(args)
