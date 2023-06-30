class TokenStatistics:
    
    def __init__(self):
        
        _ = ''
    
    def dataframe(self, tokens):

        import pandas as pd
        import signs

        describe = signs.Describe(tokens)
        counts = describe.get_counts()

        counts_df = pd.DataFrame()
        counts_df['token'] = counts.keys()
        counts_df['count'] = counts.values()

        tokens_with_counts = counts_df
        tokens_with_counts['pct_share'] = ((tokens_with_counts['count'] / tokens_with_counts['count'].sum()) * 100)
        tokens_with_counts['cum_sum'] = tokens_with_counts.pct_share.cumsum().round(1)
        tokens_with_counts['pct_share'] = tokens_with_counts['pct_share'].round(2)

        return tokens_with_counts
