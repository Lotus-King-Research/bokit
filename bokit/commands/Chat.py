class Chat:

    '''Provides access to several OpenAI endpoints.'''
    
    def __init__(self, openai_api_key):
        
        import openai

        self._openai = openai
        self.openai.api_key = openai_api_key

    def query(self,
              prompt,
              context='', 
              model="gpt-4-0613", 
              max_tokens=100):
        
        '''Takes in a prompt and returns a response.
        
        prompt | str | Prompt to be sent to OpenAI API.
        context | str | Context to be sent to OpenAI API.
        model | str | Model to be used by OpenAI API.
        max_tokens | int | Maximum number of tokens to be returned by OpenAI API.
        
        '''

        message = [{"role": "user", "content": context + '\n' + prompt}]

        response = self._openai.ChatCompletion.create(model=model,
                                                      max_tokens=max_tokens,
                                                      messages = message)

        return response
