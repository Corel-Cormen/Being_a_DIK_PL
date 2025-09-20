import deep_translator
import re

def replace_narrow_braces(match):
    content = match.group(1)
    if content.startswith('/'):
        return '{/}'
    else:
        return '{}'

def prepare_text(text):
    r_pos = text.rfind("\"")
    l_pos = text.find("\"")+1
    orginal_text = text[l_pos:r_pos]
    text_marker = re.findall(r'\{(.*?)\}', orginal_text)
    character_marker = re.findall(r'\[(.*?)\]', orginal_text)

    text_to_translate = re.sub(r'\{(.*?)\}', replace_narrow_braces, orginal_text)
    text_to_translate = re.sub(r'\[(.*?)\]', '[]', text_to_translate)
    text_to_translate = text_to_translate.replace("\\n", " \\n ")

    return orginal_text, text_to_translate, text_marker, character_marker

def prepare_transclate(translated, text_marker, character_marker):
    translated = translated.replace("{} ", "{}")
    translated = translated.replace(' {/}', '{/}')
    translated = translated.replace('{/}', '{}')
    translated = translated.replace(" \\ n", "\\n")
    translated = translated.replace(" \\ N", "\\n")
    translated = translated.replace(" \\n ", "\\n")

    for i in range(len(text_marker)):
        translated = translated.replace('{}', f'{{{text_marker[i]}}}', 1)
    for i in range(len(character_marker)):
        translated = translated.replace('[]', f'[{character_marker[i]}]', 1)

    return translated

def is_text_bios(text):
    check_text = text.strip()
    if check_text.startswith("$ bios_history_"):
        return True
    return False

def is_text_textbox(text):
    check_text = text.strip()
    if check_text.startswith("show text \""):
        return True
    return False

def is_text_alone(text):
    check_text = text.strip()
    if len(check_text) >= 2 and \
        check_text[0] == "\"" and \
        (check_text[-1] == "\"" or \
        (check_text[-2] == "\"" and check_text[-1] == ":")):
        return True
    else:
        return False

def is_text_option_if_statment(text):
    pos = text.find("\"")
    if pos > 1:
        if text[pos-1] == "\t" and "\" if " in text:
            return True
    return False

def is_text_character(text):
    check_text = text.strip()

    characters = [
        "mc", "js", "my", "sa", "isa", "ice", "qu", "ca", "cam", "ri",
        "ja", "ji", "bu", "sb", "tm", "rs", "jac", "jm", "le", "ni",
        "jb", "an", "ch", "dw", "mg", "sy", "rn", "eu", "tri", "ty",
        "rich", "tr", "lu", "go", "ml", "sar", "el", "mn", "ar", "he",
        "beth", "bo", "stan", "de", "dpc", "dad", "dad2", "troy", "st",
        "kid", "wen", "mi", "mon", "pt", "tn", "ash", "en", "ro", "ly",
        "br", "sn", "girl", "be", "hg", "bt", "rc", "ll", "uk", "jc",
        "kcs", "dikc", "dolcs", "cl", "bs", "cs", "cs2", "sec", "stu",
        "fem", "prep", "prepp", "maid", "wife", "husband",
    ]

    for character in characters:
        if check_text.startswith(character + " \"") and check_text[-1] == "\"":
            return True
    return False

num_lines = 0
with open("script.rpy", "r") as file:
    num_lines = sum(1 for _ in file)

with open("script.rpy", "r") as file:
    with open("new_script.rpy", "a", encoding="utf-8") as newfile:
        # translator = deep_translator.GoogleTranslator(source="en", target="pl")
        translator = deep_translator.MyMemoryTranslator(source="en-GB", target="pl-PL")

        line_count = 0
        for line in file:
            translate_line = ""
            line_count += 1

            if line_count < 5153:
                continue

            if  is_text_bios(line) or \
                is_text_textbox(line) or \
                is_text_alone(line) or \
                is_text_option_if_statment(line) or \
                is_text_character(line):

                orginal_text, text_to_translate, text_marker, character_marker = prepare_text(line)
                translated = translator.translate(text_to_translate)
                translated = prepare_transclate(translated, text_marker, character_marker)

                translate_line = line.replace(orginal_text, translated)
                print(f"translate line: {line_count}/{num_lines}")

            if translate_line == "":
                newfile.write(line)
            else:
                newfile.write("#" + line)
                newfile.write(translate_line)
