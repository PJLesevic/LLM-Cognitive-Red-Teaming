
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/master_llm_tagged_dataset_autotagged_updated.csv")
df.fillna(0, inplace=True)

tags = ["human_hallucination", "human_contradiction", "human_deviation", "human_leak", "human_repetition"]
df[tags] = df[tags].astype(int)

output_dir = "data/heatmaps"
os.makedirs(output_dir, exist_ok=True)

for tag in tags:
    data = df.pivot_table(index="profile", columns="prompt_id", values=tag, aggfunc="sum", fill_value=0)
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, annot=True, cmap="Blues", cbar_kws={'label': f'{tag.replace("human_", "").capitalize()} Count'})
    plt.title(f"Heatmap of {tag.replace('human_', '').capitalize()}s by Profile and Prompt")
    plt.xlabel("Prompt ID")
    plt.ylabel("Profile")
    plt.tight_layout()
    filepath = os.path.join(output_dir, f"{tag}_heatmap.png")
    plt.savefig(filepath)
    plt.close()

print("Heatmaps saved to:", output_dir)
