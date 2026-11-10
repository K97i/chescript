"""
**DO** MODIFY THIS FILE!
"""

def get_value(word: str) -> bool | int | float:
    """
    Function to actually calculate the feature.

    Args:
        word (str): Actual word/entry to analyze

    Returns:
        (bool | int | float): Calculated value for the feature

    NOTE:
        This is the function you actually want to modify! 
        
        From what I understand, you only need the entry for any feature you want to calculate, but if you **really** need anything else for a specific feature, modify `/src/features/module.py` and add an if condition for the name of the feature.
        
        Otherwise, just modify this function! 
        
        The example returns the word length of the input to test if it works. 
    """
    return word.__len__()