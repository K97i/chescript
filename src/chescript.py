"""
DO NOT MODIFY!

You may have entered in here by mistake. Please go to the ./src/features folder!
"""

from .rw_csv import load, save
from .features import get_features

def run():
    """
    Actually runs the script
    """
    input_csv = load()
    if input_csv:
        final_list = get_features(word_list=input_csv)
        save(data=final_list)

if __name__ == "__main__":
    run()