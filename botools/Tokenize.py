class Tokenize:
    
    def __init__(self):

        from botok import WordTokenizer
        from botok.config import Config
        from pathlib import Path
        
        config = Config(dialect_name="general", base_path=Path.home())
        self._wt = WordTokenizer(config=config)

    def get_tokens(self, text):

        tokens = []
        
        tokenizer_output = self._wt.tokenize(text, split_affixes=False)
        
        for token in tokenizer_output:
            tokens.append(token['text_unaffixed'])
            
        return tokens
   