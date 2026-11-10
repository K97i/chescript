"""
DO NOT MODIFY!

You may have entered in here by mistake. Please read the README.md in this folder!
"""

from ..classes import Feature, Entry
import importlib
import pkgutil
from . import feature_code

def load_packages() -> dict:
    """
    Loads all packages from the feature_code folder
    """

    imported_modules = {}

    # For every package in the folder...
    for _, module_name, is_pkg in pkgutil.iter_modules(feature_code.__path__):

        # Import the package
        imported_modules[module_name] = importlib.import_module(f"{feature_code.__name__}.{module_name}")
        
    # Return the imported features
    return imported_modules

def get_features(word_list: list[Entry]) -> list[Entry]:
    """
    Generates the features for every word in the word list

    Args:
        word_list (list[Entry]): Initial list of words with no features

    Returns:
        working_list (list[Entry]): Final list of words with all available features
    """

    # Get all features
    functions = load_packages()

    # Shallow copy the word list
    working_list = word_list.copy()
    
    # For every word in the working list...
    for word in working_list:
        feature_list = []
        
        # Get all features
        for feature_name, actual_module in functions.items():
            feature_list.append(
                Feature(
                    name=feature_name, 
                    value=actual_module.get_value(
                        word=word.word
                        )
                    )
                )
        
        # Set the features
        word.features = feature_list

    return working_list