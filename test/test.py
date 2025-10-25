from mlsaver.main import MLSaver
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = LogisticRegression()
model.fit(X, y)

saver = MLSaver() # <-- Initializes object.
saver.commit(model, "v1") # <-- Saves model.
saver.log() # <-- Shows all versions.
saver.delete("v2") # <-- Deletes.