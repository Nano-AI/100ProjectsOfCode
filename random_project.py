import re
import random

with open("README.md") as f:
    contents = f.read()

things = re.findall("- \[ \] [^]]+\]", contents)
rand = random.choices(things, k=5)

print("\n".join(rand))

