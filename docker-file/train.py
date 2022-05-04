from sklearn.linear_model import LinearRegression
from json import loads, dumps


with open ('/data/input.json') as f:
    content = f.read()
    TRAIN_INPUT =loads(content)

with open('/data/output.json') as f:
    content = f.read()
    TRAIN_OUTPUT =loads(content)

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

with open('../model.json', 'w') as f:
    f.write(dumps(predictor.coef_.tolist()))