class GlossaryMatching:

    '''Takes in Tibetan term and returns English.'''
    
    def __init__(self):
        
        import pandas as pd

        _base_url = 'https://raw.githubusercontent.com/Lotus-King-Research/Padma-Dictionary-Data/main/data/'
        
        self.lotus_king = pd.read_csv(_base_url + 'Lotus-King.csv', sep='\t')
        self.lotus_king = self.lotus_king.set_index('Tibetan').to_dict()
        
        self.tony_duff = pd.read_csv(_base_url + 'Tony-Duff.csv', sep='\t')
        self.tony_duff = self.tony_duff.set_index('Tibetan').to_dict()
        
    def glossary_lookup(self, token, dictionary):

        if dictionary == 'lotus_king':
            _dictionary = self.lotus_king
        
        elif dictionary == 'tony_duff':
            _dictionary = self.tony_duff
            
        else:
            raise ValueError("dictionary must be lotus_king or tony_duff")
        
        try:
            return _dictionary['Description'][token]
        except KeyError:
            return ''

    def check_glossary_matches(self, tokens, dictionary='lkt', clean_tokens=False):

        if clean_tokens:
            tokens = self.clean_tokens(tokens)
        
        matches = []

        for token in tokens:

            if len(self.glossary_lookup(token, dictionary)) > 0:
                matches.append(self.glossary_lookup(token, dictionary))

            elif len(self.glossary_lookup(token + 'པ་', dictionary)) > 0:
                matches.append(self.glossary_lookup(token + 'པ་', dictionary))

            elif len(self.glossary_lookup(token + 'པོ་', dictionary)) > 0:
                matches.append(self.glossary_lookup(token + 'པོ་', dictionary))

            elif len(self.glossary_lookup(token + 'བ་', dictionary)) > 0:
                matches.append(self.glossary_lookup(token + 'བ་', dictionary))

            else:
                matches.append('')

        out = {}

        for i in range(len(tokens)):
            out[tokens[i]] = matches[i]

        return out

    def clean_tokens(self, tokens):

        out = []

        for token in tokens:

            token = token.strip()
            token = token.replace(' ', '')
            token = token.replace('།', '')
            token = token.replace('༔', '')
            token = token.replace('༅', '')
            token = token.replace('༄', '')

            if token.endswith('་') is False:
                token = token + '་'

            if token != '་':
                out.append(token)

        import signs

        tokens_cleaned = signs.Describe(out).get_counts()
        tokens_cleaned = list(set([i for i in tokens_cleaned]))

        return tokens_cleaned
