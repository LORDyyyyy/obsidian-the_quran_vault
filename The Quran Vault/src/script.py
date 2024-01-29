#!/usr/bin/env python
import pyquran as pq
from typing import TextIO
basmalah = pq.quran.get_sura(1, True)[0]


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
        the function that will get the surah and the files and folders data.
    """
    dest_folder = '../dest/quran'
    file_format = 'md'

    for sura_no in range(1, 115):
        sura_name = pq.get_sura_name(sura_no)
        file_name = f'{to_hindi_no(sura_no)}-{sura_name}'
        path = f'{dest_folder}/{file_name}.{file_format}'
        generate_files(pq, path, sura_no, sura_name)


def generate_files(pq: object, path: str,
                   sura_no: int, sura_name: str) -> None:
    """
        The function that will generate the Quran in files.
        Each Surah in a separate file.
    """
    f = open(path, 'w', encoding='utf-8')
    surah = pq.get_sura(sura_no, True, False)
    init_file(f, sura_no, sura_name)

    for index, verse in enumerate(surah):
        verse_no = index + 1
        f.write(verse + '  ' + to_hindi_no(verse_no) + '<br>\n')

    f.close()


def init_file(f: TextIO, sura_no: int, sura_name: str) -> None:
    """
        The function that will write the metadata of the file
    """
    f.write(
        f"""---
cssclasses:
    - quran-container
tags:
    - {sura_name}
    - surah#{sura_no}
---\n
""")


if __name__ == "__main__":
    """ Main function """

    run(pq.quran)
    # print(q.quran. get_sura(102, True))
