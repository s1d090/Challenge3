import sys

def encrypt(message, shift):
    text = ""
    count_text = ""

    for c in message:
        if(c.isalpha()):
            count_text += (c+shift)
        if(len(count_text) == 5):
            text += (count_text + " ")
    text += count_text

    return text

shift = int(sys.argv[1])
for line in sys.stdin:
    encrypt(line)
