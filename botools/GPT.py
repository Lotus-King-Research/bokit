class GPT:

    '''Provides access to several OpenAI endpoints.'''
    
    def __init__(self, openai_api_key):
        
        import openai

        self.openai = openai
        self.openai.api_key = openai_api_key
        

    def context_definition_summary(self):

        return 'Condense provided Tibetan word definitions, following Oxford English rules for capitalization, into single English keywords.'

    def _context_definition_summary(self):

        context = '''
            - I will give you definitions of words
            - The definitions are going to be kind of mix of dictionary style and encyclopedic
            - The source will always be the same
            - The words are all from Tibetan
            - the definitions are in English
            - your task is to summarize the definition into single words, one or more
            - do not always use capital letters, but follow oxford english rules for capitalization
        '''

        return context


    def query_completion(self, prompt, context='', model='davinci-003'):

        response = self.openai.Completion.create(
            engine=model,
            prompt=context + '\n' + prompt,
            max_tokens=50)

        summary = response.choices[0].text.strip()
        print(summary)

    def query_chat(self,
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

        response = self.openai.ChatCompletion.create(
            model=model,
            max_tokens=max_tokens,
            messages = message)

        return response
