# Import packages
import numpy as np
import pandas as pd

# Read data
dataset = pd.read_csv('../data/corpus.csv')


# Create method to transform column
def normalize_seer_stage(seer_stage):
    if seer_stage in [4, 5, 7]:
        return 'later_stage'
    elif seer_stage in [8, 9]:
        return 'non-applicable'
    else:
        return 'early_stage'


# Add new column with normalization
dataset['Normalized_seer_stage'] = dataset.seer_stage.apply(lambda x: normalize_seer_stage(x))

# Prepare variables that will be used
early_stage_dataset = dataset[dataset.Normalized_seer_stage == 'early_stage']
later_stage_dataset = dataset[dataset.Normalized_seer_stage == 'later_stage']

print(dataset.head(50))
