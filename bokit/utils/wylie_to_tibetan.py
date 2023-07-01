def wylie_to_tibetan(wylie_string):
    
    '''Takes in string, and converts to Tibetan following Wylie rules.
    Adds Tsek between syllables and after the last syllable.'''

    import pyewts

    converter = pyewts.pyewts()

    return converter.toUnicode(wylie_string, []) + '་'
