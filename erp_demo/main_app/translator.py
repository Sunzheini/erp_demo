from erp_demo.main_app import custom_collections


def translate_to_maimunica(text):
    result = ''

    cyrillic_chars = custom_collections.cyrillic_chars
    corresponding_english_chars = custom_collections.corresponding_english_chars

    for char in text:
        if char in cyrillic_chars:
            idx = cyrillic_chars.index(char)
            result += corresponding_english_chars[idx]
        else:
            result += char

    return result
