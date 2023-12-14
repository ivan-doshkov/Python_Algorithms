def decode_morse(morse_code):
    MORSE_CODE = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-----': '0',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '.-.-.-': '.',
        '--..--': ',',
        '..--..': '?',
        '.----.': '`',
        '-.-.--': '!',
        '-..-.': '/',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '---...': ':',
        '-.-.-.': ';',
        '-...-': '=',
        '.-.-.': '+',
        '-....-': '-',
        '..--.-': '_',
        '.-..-.': '"',
        '...-..-': '$',
        '.--.-.': '@',
        '...-.-': 'End of work',
        '........': 'Error',
        '-.-.-': 'Starting Signal',
        '...-.': 'Understood',
        '...---...': 'SOS',
        '': ' ',
    }
    split_morse_code = morse_code.strip().split(' ')
    return ''.join([MORSE_CODE[code] for code in split_morse_code]).replace('  ', ' ')


print(decode_morse('.... . -.--   .--- ..- -.. .'))
print(decode_morse('.-'))
print(decode_morse('--...'))
print(decode_morse('...-..-'))
print(decode_morse('.'))
print(decode_morse('..'))
print(decode_morse('. .'))
print(decode_morse('.   .'))
print(decode_morse('...-..- ...-..- ...-..-'))
print(decode_morse('----- .---- ..--- ---.. ----.'))
print(decode_morse('.-... ---...   -..-. --...'))
print(decode_morse('...---...'))
print(decode_morse('... --- ...'))
print(decode_morse('...   ---   ...'))
