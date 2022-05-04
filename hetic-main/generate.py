
from json import dumps
from random import randint

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)

with open("dataset_repo/input.data.json", "w") as f:
  f.write(dumps(TRAIN_INPUT))

with open("dataset_repo/output.data.json", "w") as f:
  f.write(dumps(TRAIN_OUTPUT))
