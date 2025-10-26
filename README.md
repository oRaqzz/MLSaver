# MLSaver

**MLSaver** is a lightweight Python package that lets you version-control your machine learning models locally — similar to Git, but for ML experiments.

---

## ✨ Features
- Save trained models with simple commands  
- Load previous model versions instantly  
- List all saved versions  
- Delete unwanted versions
- Prints model info
- Works locally — no extra setup, no cloud required

---

## 🧠 Installation
```bash
pip install mlsaver
```

## ⚙️ Importing MLSaver

Import the class into your project:

```python
from mlsaver import MLSaver
```
Then create an instance:
```python
saver = MLSaver()
```

## ⚙️ Methods


| Method | Description | Example |
|--------|--------------|----------|
| `commit(model, "v1")` | Save a trained model with a version name. | `saver.commit(model, "v1")` |
| `checkout("v1")` | Load a previously saved model. | `model = saver.checkout("v1")` |
| `log()` | List all saved versions. | `saver.log()` |
| `delete("v1")` | Delete a saved version. | `saver.delete("v1")` |
| `rename("v1", "v1_fixed")` | Rename an existing version. | `saver.rename("v1", "v1_fixed")` |
| `info("v1")` | Show detailed info about a version (size, date, hyperparameters). | `saver.info("v1")` |
| `clear()` | Delete all saved versions (with confirmation). | `saver.clear()` |



