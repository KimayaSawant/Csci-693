import pandas as pd
from scipy.stats import ttest_ind

# Load Excel
file_path = "CSCI 693 Cracking the ATS Tools.xlsx"
df = pd.read_excel(file_path).iloc[:16]  # assuming first 15 rows are valid resume entries

# Drop the first row (explanatory labels)
df = df.drop(index=0)

# Extract ATS scores
# original_scores = pd.to_numeric(df['ATS-1(ResumeGO) Original'], errors='coerce').dropna().tolist() + \
#                   pd.to_numeric(df['ATS-2 (NodeFlair) Original'], errors='coerce').dropna().tolist() + \
#                   pd.to_numeric(df['ATS-3 (Resume Worded) Original'], errors='coerce').dropna().tolist()


# Extracting the ats scores by flattening them into sinle lists of respective categories

original_scores = df[[
    'ATS-1(ResumeGO) Original', 
    'ATS-2 (NodeFlair) Original', 
    'ATS-3 (Resume Worded) Original'
]].astype(float).values.flatten()


ai_scores = df[[
    'ATS-1 SCORE AI',
    'ATS-2 SCORE AI',
    'ATS-3 SCORE AI'
]].astype(float).values.flatten()

manual_scores = df[[
    'ATS-1 SCORE Manual',
    'ATS-2 SCORE Manual',
    'ATS-3 SCORE Manual'
]].astype(float).values.flatten()


# print("Original ATS Scores:", original_scores)
# print("AI-Modified ATS Scores:", ai_scores)
# print("Manual-Modified ATS Scores:", manual_scores)


# Run Welch’s t-tests (unequal variances)
print("\nOriginal vs AI:")
t1, p1 = ttest_ind(original_scores, ai_scores, equal_var=False)
print(f"t = {t1:.4f}, p = {p1:.4f}")

print("\nAI vs Manual:")
t2, p2 = ttest_ind(ai_scores, manual_scores, equal_var=False)
print(f"t = {t2:.4f}, p = {p2:.4f}")

print("\nOriginal vs Manual:")
t3, p3 = ttest_ind(original_scores, manual_scores, equal_var=False)
print(f"t = {t3:.4f}, p = {p3:.4f}")
