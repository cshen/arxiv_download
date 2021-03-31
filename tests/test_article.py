""" Test article.py """

import src.article as sa


def test_escape_special_chars():
    chars = [r'"', r"{"]
    test_string = '{here we go "'
    assert sa.escape_special_chars(test_string, chars) == '\\{here we go \\"'


def test_delete_prepositions():
    test1 = "Hello, a cow goes to the store."
    test2 = "Here The is capital."
    remove = ["a", "the", "to"]
    assert sa.delete_prepositions(test1, remove) == "Hello, cow goes store."
    assert sa.delete_prepositions(test2,
                                  remove,
                                  case_sensitive=False) == "Here is capital."


def test_bib_title():
    title1 = 'The fundamental Laws of the Universe'
    title2 = 'The $N=2$ of QFT'
    title3 = 'All elements of {1, 2} are natural'
    assert sa.bib_title(title1) == "{The} fundamental {Laws} of the {Universe}"
    assert sa.bib_title(title2) == "{The} {$N=2$} of {QFT}"
    assert sa.bib_title(title3) == "{All} elements of \\{1, 2\\} are natural"
