import pandas as pd
import numpy as np

# Load u.data file which contains the ratings data
ratings_df = pd.read_table('http://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Load u.user file which contains the user information
users_df = pd.read_table('http://files.grouplens.org/datasets/movielens/ml-100k/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])

# Merge ratings_df and users_df on 'user_id'
merged_df = pd.merge(ratings_df, users_df, on='user_id', how='inner')

# Filter for males and females separately
males_df = merged_df.query("gender == 'M'")
females_df = merged_df.query("gender == 'F'")

# Calculate average review score grouped by each person
males_avg_rating = males_df.groupby('user_id')['rating'].mean()
females_avg_rating = females_df.groupby('user_id')['rating'].mean()

# Calculate standard deviation for males and females
males_std = np.std(males_avg_rating)
females_std = np.std(females_avg_rating)

# Output the results to a text file
with open('user_scores_std.txt', 'w') as f:
    f.write("{:.2f} {:.2f}".format(males_std, females_std))

print("Standard Deviation of Males' User Scores: {:.2f}".format(males_std))
print("Standard Deviation of Females' User Scores: {:.2f}".format(females_std))
