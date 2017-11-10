#Caesar Cipher
# https://www.nostarch.com/crackingcodes/

import pyperclip
import random
import pyautogui

# The string to be encrypted/decrypted:
message = pyautogui.password(text="Input Caesar Cipher to be encrypted below.", title="Caesar Cipher", default="", mask="*")

# The encryption/decryption key:
key = random.randint(1,66)


# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption:
        translatedIndex = symbolIndex + key

        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
