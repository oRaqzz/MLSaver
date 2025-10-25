# MLSaver

**MLSaver** is a lightweight Python package that lets you version-control your machine learning models locally — similar to Git, but for ML experiments.

---

## ✨ Features
- Save trained models with simple commands  
- Load previous model versions instantly  
- List all saved versions  
- Delete unwanted versions  
- Works locally — no extra setup, no cloud required  

---

## 🧠 Installation
```bash
pip install mlsaver
```

## ⚙️ Methods

## Make an instance of MLSaver.
```python
saver = MLSaver()
```

| Method | Description | Example |
|--------|--------------|----------|
| `commit(model, "v1")` | Save a trained model with a version name. | `saver.commit(model, "v1")` |
| `checkout("v1")` | Load a previously saved model. | `model = saver.checkout("v1")` |
| `log()` | List all saved versions. | `saver.log()` |
| `delete("v1")` | Delete a saved version. | `saver.delete("v1")` |


