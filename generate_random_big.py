def write_lines_to_file(file, lines):
    #with open(filename, 'w') as file:
    for line in lines:
        file.write(line + '\n')

def generate_binary():
    import random
    return ''.join(str(random.randint(0, 1)) for _ in range(32))

if __name__ == "__main__":

    file = open("C:\\verilog_files\\tb_txt_files\\mat_inputs.txt", 'w')

    lines = [
        '023333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '112333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '00000000001011010000000001001101',
        '00000000010000010000000001011101',
        '00000000110110010000000110111100',
        '00000000000101110000000000001011'
    ]

    write_lines_to_file(file, lines)

    for i in range(9):
        lines = [
            '023333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '112333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '00000000001011010000000001001101',
            '00000000010000010000000001011101',
            '00000000110110010000000110111100',
            '00000000000101110000000000001011'
        ]
        for j in range(8):
            lines[j +1 ] = generate_binary()
            lines[j + 10] = generate_binary()

        write_lines_to_file(file, lines)

    lines = [
        '033333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '103333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '00000000001011010000000001001101',
        '00000000010000010000000001011101',
        '00000000110110010000000110111100',
        '00000000000101110000000000001011'
    ]

    write_lines_to_file(file, lines)

    for i in range(9):
        lines = [
            '033333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '103333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '00000000001011010000000001001101',
            '00000000010000010000000001011101',
            '00000000110110010000000110111100',
            '00000000000101110000000000001011'
        ]
        for j in range(8):
            lines[j + 1] = generate_binary()
            lines[j + 10] = generate_binary()

        write_lines_to_file(file, lines)

    lines = [
        '033333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '133333',
        '11111111110100110000000001010010',
        '00000000010100101111111111101111',
        '00000000001110000000000001100110',
        '11111111100111101111111111000001',
        '00000000001011010000000001001101',
        '00000000010000010000000001011101',
        '00000000110110010000000110111100',
        '00000000000101110000000000001011'
    ]

    write_lines_to_file(file, lines)

    for i in range(9):
        lines = [
            '033333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '133333',
            '11111111110100110000000001010010',
            '00000000010100101111111111101111',
            '00000000001110000000000001100110',
            '11111111100111101111111111000001',
            '00000000001011010000000001001101',
            '00000000010000010000000001011101',
            '00000000110110010000000110111100',
            '00000000000101110000000000001011'
        ]
        for j in range(8):
            lines[j + 1] = generate_binary()
            lines[j + 10] = generate_binary()

        write_lines_to_file(file, lines)

    lines = [
        '033121',
        '01011001110100110100100101010010',
        '00010010010100101111010011101011',
        '00101000001110010100010101100110',
        '01111111100111101001100111000001',
        '00100011110100110001000001010010',
        '00010010010100101110011011101100',
        '00001000001110000000100101100110',
        '11111111100110100011000111000001']
    write_lines_to_file(file, lines)
    """
    lines = [
        '033333',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '00000000000000000000000000000000']
    write_lines_to_file(file, lines)
    #for i in range(32768):
    lines = [
        '133333',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000',
        '10000000100000001000000010000000']
    write_lines_to_file(file, lines)
    """
    file.close()