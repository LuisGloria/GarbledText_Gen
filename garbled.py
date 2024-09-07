import random

# characters go here, feel free to add more if u want, IDK.
garbled_map = {
    'A': 'Ⱥ', 'a': 'ḁ', 'B': 'Ƀ', 'b': 'ḃ', 'C': 'Ƈ', 'c': 'ƈ',
    'D': 'Đ', 'd': 'ḓ', 'E': 'Ȅ', 'e': 'ḕ', 'F': 'Ƒ', 'f': 'ḟ',
    'G': 'Ǥ', 'g': 'ǥ', 'H': 'Ȟ', 'h': 'ḧ', 'I': 'Ȉ', 'i': 'ḭ',
    'J': 'Ɉ', 'j': 'ɉ', 'K': 'Ⱥ', 'k': 'ḱ', 'L': 'Ƚ', 'l': 'ḽ',
    'M': 'Ṁ', 'm': 'ḿ', 'N': 'Ƞ', 'n': 'ṋ', 'O': 'Ȯ', 'o': 'ȯ',
    'P': 'Ᵽ', 'p': 'ṗ', 'Q': 'Ɋ', 'q': 'ɋ', 'R': 'Ȑ', 'r': 'ṟ',
    'S': 'Ș', 's': 'ṩ', 'T': 'Ⱦ', 't': 'ṫ', 'U': 'Ʉ', 'u': 'ṳ',
    'V': 'Ṽ', 'v': 'ṽ', 'W': 'Ŵ', 'w': 'ŵ', 'X': 'Ẋ', 'x': 'ẋ',
    'Y': 'Ỳ', 'y': 'ỵ', 'Z': 'Ż', 'z': 'ẓ',
    'Ǿ': "ǽ", "Ǽ": "Ǻ", "Ǥ": "ǋ", "Ƞ": "ɿ", "ɾ": "ɹ", "ɸ": "ɷ",
    "ɣ": "ɩ", "ɗ": "ʄ", "ʦ": "ˀ", "ʯ": "Ю", "ѵ": "Э", "ϻ": "Ϭ",
    "Ї": "Ь", "ҝ": "҈", "Ṙ": "Ḥ", "∂": "∏", "∆": "∑", "Ї": "Д",
    "ҝ": "҈", "Ṙ": "Ḥ", "∂": "∏", "∆": "∑", "−": "∙", "√": "−",
    "∞": "∟", "∫": "≈", "≡": "⌂", "⌠": "⌡", "█": "Ⱪ", "Ɐ": "∩",
    ' ': ' ', "'": "'", ',': ',', '.': '.', '!': '!', '?': '?'
}

def garble_text(text):
    garbled_text = ''
    for char in text:
        if char in garbled_map:
            garbled_text += garbled_map[char]
        else:
            garbled_text += char  # Leave characters that aren't in the map unchanged
    return garbled_text

user_input = input("Enter some text: ")

# Output.
garbled_output = garble_text(user_input)
print("Garbled text:", garbled_output)

