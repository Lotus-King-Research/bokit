class Translate:

    '''For translating automatically from Tibetan to English.'''

    def __init__(self):

        import requests
        import json

        self.requests = requests
        self.json = json

    def translate(self,
                  input_sentence,
                  level_of_explanation=0,
                  language='tib', 
                  model='NO',
                  debug=False):
        
        '''Takes in Tibetan string and returns English translation.
        
        input_sentence | str | Tibetan string
        level_of_explanation | int | 0, 1, or 2
        language | str | 'tib' or 'eng-tib
        model | str | 'NO' or 'YES'
        debug | bool | If True, prints response status code and content.
        
        '''

        url = "https://linguae-dharmae.net/api/translation/"
        
        headers = {"Content-type": "application/json"}
        
        data = {"input_sentence": input_sentence,
                "level_of_explanation": level_of_explanation,
                "language": language,
                "model": model}
        
        response = self.requests.post(url, headers=headers, data=self.json.dumps(data))
        
        if debug:

            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")
            
        return response.text.split(':')[-1].strip().replace('"','')
