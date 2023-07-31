import argparse
import chepy
import base64
import hashlib
import base58

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded_text):
    return base64.b64decode(encoded_text).decode()

def encode_rot(text, shift):
    return chepy.caesar_cipher(text, shift)

def decode_rot(encrypted_text, shift):
    return chepy.caesar_cipher(encrypted_text, -shift)

def encode_hex(text):
    return text.encode().hex()

def decode_hex(hex_text):
    return bytes.fromhex(hex_text).decode()

def encode_base58(text):
    return base58.b58encode(text.encode()).decode()

def decode_base58(encoded_text):
    return base58.b58decode(encoded_text).decode()

def calculate_md5(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

def encode_morse(text):
    morse_table = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': ' '
    }
    encoded_text = ' '.join([morse_table.get(c.upper(), c) for c in text])
    return encoded_text

def main():
    parser = argparse.ArgumentParser(description="cuff - cryptography tool")
    parser.add_argument("action", choices=["encode", "decode"], help="Choose 'encode' or 'decode'")
    parser.add_argument("method", choices=["base64", "rot", "hex", "base58", "md5", "morse"], help="Choose the encoding/decoding method")
    parser.add_argument("text", help="The text to be encoded or decoded")
    parser.add_argument("--key", type=int, default=3, help="The shift key for ROT cipher (default: 3)")

    args = parser.parse_args()

    if args.method == "base64":
        if args.action == "encode":
            result = encode_base64(args.text)
        else:
            result = decode_base64(args.text)
    elif args.method == "rot":
        if args.action == "encode":
            result = encode_rot(args.text, args.key)
        else:
            result = decode_rot(args.text, args.key)
    elif args.method == "hex":
        if args.action == "encode":
            result = encode_hex(args.text)
        else:
            result = decode_hex(args.text)
    elif args.method == "base58":
        if args.action == "encode":
            result = encode_base58(args.text)
        else:
            result = decode_base58(args.text)
    elif args.method == "md5":
        result = calculate_md5(args.text)
    elif args.method == "morse":
        if args.action == "encode":
            result = encode_morse(args.text)
        else:
            result = "Morse code decoding not implemented yet."
    else:
        result = "Invalid method selected."

    print("Result:", result)

if __name__ == "__main__":
    main()
