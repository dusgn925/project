import os

import pandas as pd
from sklearn.datasets import load_iris
from vis_utils import hist_visualize

iris = load_iris()
feature_names = iris.feature_names
species = iris.target_names

X, y = iris.data, iris.target

X = pd.DataFrame(X, columns=feature_names)
y = pd.Series(y, name='species')

iris_df = pd.concat([X, y], axis=1)
save_dir = 'dataset'
file_name = 'iris_dataset.csv'
os.makedirs(save_dir, exist_ok=True)
iris_df.to_csv(os.path.join(save_dir, file_name))


species_idx_df = pd.Series(species)
file_name = 'species_idx.csv'
species_idx_df.to_csv(os.path.join(save_dir, file_name), header=False)

hist_visualize(iris_df)