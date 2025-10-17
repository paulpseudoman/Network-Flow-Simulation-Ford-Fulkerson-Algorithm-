import pandas as pd

# Load CSV file
df = pd.read_csv("D:\example.csv")  # columns: source,target,capacity

# Optional: sort or reset index
df = df.reset_index(drop=True)

# Generate add_edge statements
print("if __name__ == '__main__':")
print("    mf = DinicMaxFlow({})".format(max(df[['source','target']].max()) + 1))

for _, row in df.iterrows():
    src = row['source']
    tgt = row['target']
    cap = row['weight']
    print(f"    mf.add_edge({src}, {tgt}, {cap})")
