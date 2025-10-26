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
<<<<<<< HEAD
pip install mlsaver
=======
pip install MLSaver
>>>>>>> a9b4402 (prototype_version)
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
<<<<<<< HEAD
=======
| `rename("v1", "v1_fixed")` | Rename an existing version. | `saver.rename("v1", "v1_fixed")` |
| `info("v1")` | Show detailed info about a version (size, date, hyperparameters). | `saver.info("v1")` |
| `clear()` | Delete all saved versions (with confirmation). | `saver.clear()` |

>>>>>>> a9b4402 (prototype_version)


