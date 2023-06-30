class Phonetize: 

    def __init__(self):

        import bophono
        self.bophono = bophono

    def phonetize(self, string):

        options = {'aspirateLowTones': False}
        phon = self.bophono.UnicodeToApi(schema="LKT", options=options)
        phonetic = phon.get_api(string)
        
        return {"phonetic": phonetic}