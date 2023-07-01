class Phonetize:

    '''Tools for phonetizing Tibetan strings.'''

    def __init__(self):

        import bophono
        
        self.bophono = bophono

    def query(self, string):

        '''Takes in Tibetan string and returns phonetic transcription.
        
        string | str | Tibetan string
        '''

        options = {'aspirateLowTones': False}
        phon = self.bophono.UnicodeToApi(schema="LKT", options=options)
        phonetic = phon.get_api(string)
        
        return {"phonetic": phonetic}