import os
import joblib
import json

class MLSaver:
    # Initializer.
    def __init__(self, root_dict='.logs'):
        try:
            self.root_dict = root_dict
            if not os.path.exists(self.root_dict):
                os.mkdir(self.root_dict)

            self.metadata_json = os.path.join(self.root_dict, "metadata.json")
            if not os.path.exists(self.metadata_json):
                with open(self.metadata_json, "w") as f:
                    json.dump({}, f)

        except Exception as e:
            print(f"Error: {e}")

    # Save model.
    def commit(self, model, version_name):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)

            if version_name in version:
                raise ValueError(f"{version_name} already exists. Please use different commit message.")
            
            filename = f"{version_name}.pkl"
            filepath = os.path.join(self.root_dict, filename)
            joblib.dump(model, filepath)

            version[version_name] = filename
            with open(self.metadata_json, "w") as f:
                json.dump(version, f)

            print(f"Model saved as {version_name}")

        except Exception as e:
            print(f"Error: {e}.")

    # Switch versions.
    def checkout(self, version_name):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)

            if version_name not in version:
                print(f"{version_name} does not exist.")

            filepath = os.path.join(self.root_dict, version[version_name])
            model = joblib.load(filepath)

            print(f"checked out {version_name}!")
            return model
        except Exception as e:
            print(f"Error: {e}.")



    # Show all commits.
    def log(self):
        try:
            with open(self.metadata_json, "r") as f:
                versions = json.load(f)

            if len(versions) == 0:
                print("No model is saved.")

            print("Saved versions: ")
            for v in versions:
                print(v)
        except Exception as e:
            print(f"Error: {e}.")

    # Delete version.
    def delete(self, version_name):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)

            if version_name not in version:
                print(f"{version_name} does not exist.")
            
            filepath = os.path.join(self.root_dict, version[version_name])
            os.remove(filepath)
            del version[version_name]

            with open(self.metadata_json, "w") as f:
                json.dump(version, f)
            
            print(f"Successfully deleted {version_name}.")
        except Exception as e:
            print(f"Error: {e}.")