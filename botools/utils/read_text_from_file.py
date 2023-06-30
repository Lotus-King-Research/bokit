def read_text_from_file(file, remove_new_line=False):

    '''Reads text from a local file
    
    file | str | path to the file to be read
    remove_new_line | bool | if set to True, will remove new lines
    
    '''
    
    text = open(file)
    
    text = text.readlines()
    
    if remove_new_line:
        return [i.strip() for i in text]
        
    else:    
        return text
    