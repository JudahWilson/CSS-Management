import re

import pyperclip

# Parse CSS into a dictionary
def parseCSS(string):
    #TODO make CSS parser correctly parses test.css, test2.css, and test3.css before considering this done
    
    # Get rid of comments
    string = re.sub(r'/\*.*?\*/', '', string, flags=re.DOTALL)    
    
    
    # replace quotes with escaped quotes
    string = string.replace('"', '\\"') 
    
    # Surround selectors with quotes
    string = re.sub(r'([@a-z,A-Z0-9\-\_\[\]:()]+)\s*\{', r'"\1": {', string)
    
    # Surround property names with quotes
    string = re.sub(r'([{]\s*|;\s*)([a-zA-Z0-9\-\_,\s]+)\s*:', r'\1"\2":', string)
    
    # Surround property values with quotes
    string = re.sub(r'"+\s*:\s*([a-zA-Z0-9\-\_%]+)\s*;{0,1}([}]){0,1}', r'": "\1"\2,', string)    
    
    # ?Remove trailing commas?
    string = re.sub(r',\s*\}', r'}', string)
    
    
    
    # # Split the string into a list of lines
    # lines = string.splitlines()
    # # Initialize the dictionary
    # dictionary = {}
    # # Loop through the lines
    # for line in lines:
    #     # Split the line into a list of words
    #     words = line.split()
    #     # If the line is not empty
    #     if words:
    #         # If the line is a selector
    #         if words[0][-1] == '{':
    #             # Get the selector
    #             selector = words[0][:-1]
    #             # Initialize the dictionary for the selector
    #             dictionary[selector] = {}
    #             # Loop through the words
    #             for word in words[1:]:
    #                 # If the word is a property
    #                 if word[-1] == ':':
    #                     # Get the property
    #                     property = word[:-1]
    #                     # Initialize the dictionary for the property
    #                     dictionary[selector][property] = []
    #                 # If the word is a value
    #                 else:
    #                     # Get the value
    #                     value = word[:-1]
    #                     # Add the value to the dictionary
    #                     dictionary[selector][property].append(value)
    # # Return the dictionary
    # return dictionary
    return(string)
f = open('test.css', 'r')
s = f.read()
f.close()
# pyperclip.copy(parseCSS('}audio:not([controls]){display:none;height:0}[h'))
pyperclip.copy(parseCSS(s))