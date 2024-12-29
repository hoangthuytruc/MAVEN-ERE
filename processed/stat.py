# %%
# ACE
import json
clusters = []
for split in ["train", 'dev', "test"]:
    with open(f"./KBP/{split}.jsonl")as f:
        lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        clusters += data["events"]
print("num clusters:", len(clusters))
# print("num mentions:", len(sum(clusters, [{}])))
mentions = [i for c in clusters for i in c]
print("num mentions:", len(mentions))
# %%
# MATRES
from collections import defaultdict
import json
def count_relations(file):
    stat = defaultdict(int)
    with open(file)as f:
        lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        for k in data["relations"]:
            stat[k] += len(data["relations"][k])
    stat["sum"] = sum(stat.values())
    print(stat)
# %%
file = "./MATRES/MATRES.json"
count_relations(file)
# %%
file = "./TB-Dense/TB-Dense.json"
count_relations(file)
# %%
file = "./EventStoryLine/EventStoryLine.json"
count_relations(file)
# %%
file = "./CausalTimeBank/CausalTimeBank.json"
count_relations(file)
# %%
file = "./hievents/hievents.json"
count_relations(file)
# %%
