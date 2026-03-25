# check_threshold.py

# Read validation accuracy
with open("model_info.txt", "r") as f:
    val_acc = float(f.read().strip())

print(f"Validation accuracy: {val_acc}")

# Check threshold
if val_acc < 0.85:
    raise Exception(f"Accuracy too low ({val_acc}) — stopping deployment!")
else:
    print(f"Accuracy meets threshold ({val_acc}) — deploy can continue.")