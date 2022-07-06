#!/usr/bin/python3
"""This module appends a line of text after a line where a string is found"""


def append_after(filename="", search_string="", new_string=""):
    """Basically here I declared an empty string variable, then looped
    thru the lines and kept adding each line to text, then I check to see if
    the search string is present and if it is, I add the new string after the
    line I added, after all these I have my new content to be written and just
    write it into the file, overwriting previous content
    """

    text = ""  # the text tat will contain the new contents of the file
    with open(filename, "r") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as f1:
        f1.write(text)
