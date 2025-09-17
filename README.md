Secret Code Generator - Documentation
Introduction
The Secret Code Generator is a simple Python command-line tool that encodes and decodes secret messages using a Caesar cipher (shift-based substitution). It is useful for basic encryption exercises, learning cryptography concepts, and small projects.
Features
- Encode messages with a custom shift value
- Decode messages back to their original form
- Supports uppercase and lowercase letters
- Non-alphabet characters remain unchanged
- Interactive text-based menu
Project Structure
The project consists of a single Python file:
Secret_Code_Generator.py
How It Works
The program uses a Caesar cipher technique:
- Each letter in the input message is shifted forward or backward by a given number (shift).
- Example: With a shift of 3, the word 'HELLO' becomes 'KHOOR'.
Usage
1. Run the program with Python:
   python Secret_Code_Generator.py
2. Select an option from the menu:
   1. Encode a message
   2. Decode a message
   3. Exit
Example run:

Secret Code Generator
1. Encode a message
2. Decode a message
3. Exit
Choose an option: 1
Enter the message to encode: hello world
Enter the shift number: 3
Encoded message: khoor zruog
Requirements
The program requires:
- Python 3.x
- No external libraries
Future Improvements
- Add support for file input/output
- Add option for random shift keys
- Extend encryption methods beyond Caesar cipher
