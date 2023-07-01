class DictionaryLookup:

    '''Builds a dictionary with query engine.'''

    def __init__(self, dictionaries=[]):

        '''
        dictionaries | list | a list of dictionary names as strings

        NOTE: add ability to ingest csv directly
        '''

        import pandas as pd

        self.dictionaries = {}

        self._base_url = 'https://raw.githubusercontent.com/Lotus-King-Research/Padma-Dictionary-Data/main/data/'

        # load the dictionary reference file
        self.available_dictionaries = pd.read_csv(self._base_url + 'dictionaries.csv')

        # assume that all dictionaries are selected
        self.selected_dictionaries = self.available_dictionaries

        # handle the case for custom selection of dictionaries
        if len(dictionaries) > 0:
            self.selected_dictionaries = self.available_dictionaries[self.available_dictionaries['Label'].isin(dictionaries)]

        # add the dictionaries
        for row in self.selected_dictionaries.iterrows():
            self.dictionaries[row[1]['Label']] = self._load_dictionary(row[1]['Label'])

    def _load_dictionary(self, label):

        '''Load dictionaries to memory
        
        label | str | name of the dictionary'''

        import pandas as pd

        row = self.available_dictionaries[self.available_dictionaries['Label'] == label]

        filename = row['Name'].values[0]
        title = row['Title'].values[0]

        print("Downloading : %s" % title)

        if filename.endswith('.zip'): 
            compression = 'zip'
        else:
            compression = None

        data = pd.read_csv(self._base_url + filename,
                           sep='\t',
                           compression=compression,
                           header=0,
                           names=['Tibetan', 'Description']).dropna()

        return data

    def _query(self,
               query,
               dictionary,
               partial_match=False,
               fuzzy_match=False,
               description_match=False):

        '''Helper for querying dictionaries. If the dictionary have not been loaded yet,
        it will automatically be added into the dictionary object (self).
        
        query | str | the query string
        dictionary | str | name of the dictionary to be used 
        partial_match | bool | if partial match should be used
        fuzzy_match | bool | if fuzzy match should be used
        '''

        # see if dictionary is already loaded
        try:
            dictionary = self.dictionaries[dictionary] 
        
        # if not, then load it and keep it
        except KeyError:
            self.dictionaries[dictionary] = self._load_dictionary(dictionary)
            dictionary = self.dictionaries[dictionary]

        out = {}

        # handle partial and fuzzy match queries
        if partial_match or fuzzy_match or description_match:

            if partial_match:
                temp_query = query

            elif description_match:
                temp_query = query
            
            if partial_match:
                tibetan = dictionary[dictionary['Tibetan'].str.contains(temp_query)]['Tibetan'].tolist()
                description = dictionary[dictionary['Tibetan'].str.contains(temp_query)]['Description'].tolist()

            elif description_match:
                tibetan = dictionary[dictionary['Description'].str.contains(query)]['Tibetan'].tolist()
                description = dictionary[dictionary['Description'].str.contains(query)]['Description'].tolist()
           
            for i, word in enumerate(tibetan):
                out[word] = str(description[i])

            if query in list(out.keys()) is False:
                out[query] = None

            return out

        # handle exact match queries
        else:
            out[query] = dictionary[dictionary['Tibetan'] == query]['Description'].tolist()

        return out

    def query(self,
              string,
              sources=[],
              partial_match=False,
              description_match=False):

        '''Lookup Tibetan words from one or more dictionaries.
        
        string | str | the Tibetan string to be looked up
        sources | list or None | a list with one or more dictionary names
        partial_match | bool | if partial match should be used

        '''

        # remove trailing and leading whitespace
        string = string.lstrip()
        string = string.rstrip()

        # init
        if len(sources) == 0:
            sources = list(self.dictionaries.keys())

        out_dict = {}
        
        # handle the lookup
        for source in sources:
            
            out_dict[source] = []
            
            # check for partial match (e.g. 'sems' will also return 'semsnyis').
            if partial_match:
                out_dict[source] = self._query(string, source, partial_match=True)

            elif description_match:
                out_dict[source] = self._query(string, source, description_match=True)
            
            # exact match
            else:
                out_dict[source] = self._query(string, source)
        
        # return a dictionary where first keys are sources
        # and first keys of first keys are words.
        return out_dict
