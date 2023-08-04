from erp_demo.custom_logic import custom_collections


def translate_to_maimunica(text):
    result = ''
    cyrillic_chars = custom_collections.cyrillic_chars
    corresponding_english_chars = custom_collections.corresponding_english_chars

    for char in text:
        try:
            if char in cyrillic_chars:
                idx = cyrillic_chars.index(char)
                result += corresponding_english_chars[idx]
            else:
                result += char
        except Exception as e:
            print(f"Unexpected error: {e}")
            return f'An unexpected error occurred: {e}.'

    return result
