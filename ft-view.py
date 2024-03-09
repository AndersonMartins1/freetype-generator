#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FreeType View - Get a FreeType font file and display its bitmap representation (for all characters or a single char).
This script is useful to get font sizing (in pixels) and its representation (under bitmap format).

Usage:
  ft-view.py <ttf_file> <ttf_size> [--char=<char>] [--descenders=<comma-separated-list>] [--special-align=<comma-separated-list>]

Options:
  -h --help          Display this help screen

Examples:
  python3 ft-view.py ttf-fonts/Vera.ttf 13           # Will display all the characters
  python3 ft-view.py ttf-fonts/Vera.ttf 13 --char=A  # Display only the char "A"
  python3 ft-view.py tft-fonts/heydings_icons.ttf 23 --char=A --descenders=   # Ignore all descenders
  python3  ft-view.py ttf-fonts/Vera.ttf 13 --descenders=p,q,j,#34  # Change the descenders
  python3  ft-view.py ttf-fonts/Vera.ttf 13 --descenders=            # No descenders, so baseline = bottomline! 
  python3  ft-view.py ttf-fonts/Vera.ttf 13 --special-align=a:T,=:B,#126:M  # Change the special alignment instruction
  python3  ft-view.py ttf-fonts/Vera.ttf 13 --special-align=       # Delete special alignments. All chars on bottom line (ideal for Wingdings chars).

Happy Electronic Hacking. 
MCHobby.be
"""

# FreeType generator common items
from ftcommon import *
from docopt import docopt
import sys

def main():
    arguments = docopt(__doc__)

    char_filter = arguments['--char']  # eg: 'B' or None

    print(f"Load font {arguments['<ttf_file>']}, set size to {int(arguments['<ttf_size>'])}")

    font_loader = FreeTypeLoader(font_file=arguments['<ttf_file>'], font_size=int(arguments['<ttf_size>']))
    
    if arguments['--descenders'] is not None:  # redefine the default descenders
        font_loader.set_descenders(arguments['--descenders'])

    if arguments['--special-align'] is not None:  # redefine the default special alignments
        font_loader.set_special_align(arguments['--special-align'])

    print(f"Max size (width,height): {font_loader.max_width},{font_loader.max_height}")
    print(f'Descender size = {font_loader.descender_size}')

    for ordinal in font_loader.char_ordinals:
        if char_filter is not None and ord(char_filter) != ordinal:
            continue

        # print the bitmap representation of a character
        #   include separator & dimension
        font_loader.print_character(ordinal)

if __name__ == '__main__':
    main()

