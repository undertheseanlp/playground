import re
lines = open("data/validate_log.txt").read().splitlines()
lines = [line for line in lines if "L3 Format tokenize-error" in line]
matched = [re.findall("(train|test)-s(?P<id>\d+)", line)[0] for line in lines]
train = [_[1] for _ in matched if _[0] == "train"]
test =  [_[1] for _ in matched if _[0] == "test"]
with open("data/validate_ids.yml", "w") as f:
    f.write("train_ignores: |-\n")
    f.write("    " + ",".join(train) + "\n")
    f.write("test_ignores: |-\n")
    f.write("    " + ",".join(test))
print("Done")