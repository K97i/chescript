"""
DO NOT MODIFY!

You may have entered in here by mistake. Please go to the ./src/features folder!
"""

from __future__ import annotations
from dataclasses import dataclass

class Feature:
    def __init__(self, name: str, value: bool | int | float) -> Feature:
        """
        Initializes a Feature object

        Args:
            name (str): Name of the feature
            value (bool | int | float): The computed value of the feature 
        """
        self.name = name
        self.value = value

    def to_dict(self) -> dict:
        """
        Returns the Feature object converted to a dictionary

        Returns:
            (dict): Dictionary of the object
        """
        return {
            "Name": self.name,
            "Value": self.value,
        }

@dataclass
class Entry:
    word_id: int
    sentence_id: int 
    word: str 
    label: str
    features: list[Feature]

    @classmethod
    def from_dict(cls, data: dict) -> Entry:
        """
        Creates an Entry object from the CSV

        Args:
            data (dict): Input from the CSV data

        Returns:
            (Entry): An entry object from the data provided
        """
        return cls(
            word_id = data["word_id"],
            sentence_id = data["sentence_id"],
            word = data["word"],
            label = data["label"],

            # Empty features list for now, will be populated from features submodule
            features = []
        )

    def to_dict(self) -> dict:
        """
        Creates a dictionary version of the object

        Returns:
            return_object (dict): Dictionary conversion of the Entry object
        """
        return_object = {
            'word_id': self.word_id,
            'sentence_id': self.sentence_id,
            'word': self.word,
            'label': self.label,
        }

        for feature in self.features:
            return_object[feature.name] = feature.value

        return return_object