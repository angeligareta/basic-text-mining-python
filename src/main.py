# Import packages
import pandas as pd

# Read data
dataset = pd.read_csv('../data/corpus.csv')


# Create method to transform column
def normalize_seer_stage(seer_stage_column):
    transformed_seer_stage_column = []
    for seer_stage_index in range(len(seer_stage_column)):
        seer_stage = seer_stage_column[seer_stage_index]
        if seer_stage in [4, 5, 7]:
            transformed_seer_stage_column.append('later_stage')
        else:
            transformed_seer_stage_column.append('early_stage')

    return transformed_seer_stage_column


# Add new column with normalization
dataset['Normalized_seer_stage'] = normalize_seer_stage(dataset['seer_stage'])

print(dataset.head(50))
