import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from scr.execption import CustomExecption
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts')

class DataTransformation:
    def __init__:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            pass
        except:
            pass