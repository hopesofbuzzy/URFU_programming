import os

def draw_gallow(stage: int):
    result = ('|----+\n'
              '|    |\n')

    result += '|    '
    draw_element('0', stage, 1)
    result += '\n'

    result += '|  '
    if stage <= 1:
        result += '/-\n'
    elif stage == 2:
        result += '  *\n'
    elif stage == 3:
        result += '/-*\n'
    elif stage == 4:
        result += '/-*-\\\n'

    if stage >= 2:
        result += '|    |\n'

    print(result)

def draw_element(char: str, stage: int, check: int):
    if stage >= check:
        return char

    '''
    |----+
    |    |
    |    0
    |  /-*-\
    |    |
    |   | |
    |   | |
    |____________
    '''

draw_gallow(4)