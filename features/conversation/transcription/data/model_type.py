# models_config.py
from enum import Enum


class ModelType(Enum):
    TINY = 'tiny.en'
    BASE = 'base.en'
    SMALL = 'small.en'
    MEDIUM = 'medium.en'
    LARGE = 'large'
