#!/usr/bin/env python
import pyquran as pq
from typing import TextIO
basmalah = f'<div class="name-of-god"> <p> {pq.quran.get_sura(1, True)[0]} \
</p></div>\n'
surah_header_image = "https://raw.githubusercontent.com/LORDyyyyy/\
obsidian-the_quran_vault/main/src/webview/surah_head.png"


def to_hindi_no(number: int) -> str:
    """
        Converts an int from the 0123456789 digits to ۰١٢٣٤٥٦٧٨٩ digits

        Args:
            number (int): the number that will be converted
        Return (str): the string representation of the number
                      in the ۰١٢٣٤٥٦٧٨٩ format
    """
    ar_num = '۰١٢٣٤٥٦٧٨٩'
    en_num = '0123456789'

    table = str.maketrans(en_num, ar_num)
    normalized = str(number).translate(table)
    return (normalized)


def run(pq: object) -> None:
    """
        The function that will get the surah and the files and folders data.

        Args:
            pq (object): a pyquran.quran object
    """
    dest_folder = '../dest/The Quran'
    file_format = 'md'

    for sura_no in range(1, 115):
        sura_name = pq.get_sura_name(sura_no)
        file_name = f'{sura_no} - {sura_name}'
        path = f'{dest_folder}/{file_name}.{file_format}'
        generate_files(pq, path, sura_no, sura_name)


def generate_files(pq: object, path: str,
                   sura_no: int, sura_name: str) -> None:
    """
        The function that will generate the Quran in files.
        Each Surah in a separate file.

        Args:
            pq (object): a pyquran.quran object
            path (str): the full path contains the saving directory name,
                        file name, and the file format
            sura_no (int): the surah number
            sura_name (str): the surah name
    """

    f = open(path, 'w', encoding='utf-8')
    surah = pq.get_sura(sura_no, True, False)
    init_file(f, sura_no, sura_name)

    for index, verse in enumerate(surah):
        verse_no = index + 1

        f.write(f"""<span class="sign" id="f{verse_no}">{verse} <span>﴿</span>{to_hindi_no(verse_no)}<span>﴾</span></span>
""")

    finish_file(f)
    f.close()


def init_file(f: TextIO, sura_no: int, sura_name: str) -> None:
    """
        The function that will write the metadata and the first html elements
        of the file

        Args:
            f (TextIOWrapper): the opened file which
                                will be written into it the surah
            sura_no (int): the surah number
            sura_name (str): the surah name
    """

    f.write(
        f"""---
cssclasses:
    - quran-container
tags:
    - {sura_name}
    - surah{sura_no}
---
<div class="quran-container">
<span class="second-border"></span>
<span class="border"></span>
<div class="head-container">
<img src="{surah_header_image}" height=100>
<div class="surah-name">
<span class="surah-name-fnt">سورة {sura_name}</span>
</div>
</div>
<div class="quran-content">
{basmalah if sura_no != 1 else ""}<p>
""")


def finish_file(f: TextIO) -> None:
    """
        The function that will write the last lines of the file.

        Args:
            f (TextIOWrapper): the opened file which
                                will be written into it the surah
    """

    f.write("""
</p>
</div>
<span class="border" style="margin-top:25px;"></span>
<span class="second-border-bottom"></span>
</div>
""")


if __name__ == "__main__":
    """ Main function """

    run(pq.quran)
