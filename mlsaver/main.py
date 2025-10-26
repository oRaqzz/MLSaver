import os
import joblib
import json
import datetime

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

        # Clears histoty.
    def clear(self):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)

            if not version:
                print("No saved versions to delete.")
                return 

            confirm = str(input("This will delete all saved versions. Type 'yes' to confirm: "))
            if confirm.lower() != 'yes':
                return 
            
            for filename in version.values():
                filepath = os.path.join(self.root_dict, filename)
                if os.path.exists(filepath):
                    os.remove(filepath)
            
            with open(self.metadata_json, "w") as f:
                json.dump({}, f)

            print("ALL VERSIONS DELETED.")

        except Exception as e:
            print(f"Error: {e}")

    # Rename Version.
    def rename(self, old_name, new_name):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)
            
            new_filename = f"{new_name}.pkl"

            if old_name not in version:
                print(f"{old_name} does not exist.")
                return

            if new_name in version:
                print(f"{new_name} already exists.")
                return

            old_path = os.path.join(self.root_dict, version[old_name])
            new_path = os.path.join(self.root_dict, new_filename)
            os.rename(old_path, new_path)

            version[new_name] = new_filename
            del version[old_name]

            with open(self.metadata_json, "w") as f:
                json.dump(version ,f)

            print(f"Renamed {old_name} --> {new_name}")

        except Exception as e:
            print(f"Error: {e}")

    # Get info.
    def info(self, version_name):
        try:
            with open(self.metadata_json, "r") as f:
                version = json.load(f)

            if not version_name in version:
                print(f"{version_name} does not exist.")
                return

            filepath = os.path.join(self.root_dict, version[version_name])
            if not os.path.exists(filepath):
                print(f"File for {version_name} not found.")
                return
            
            model = joblib.load(filepath)

            file_size = os.path.getsize(filepath) / 1024
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

            params = {}
            if hasattr(model, "get_params"):
                params = model.get_params()

            n_params = len(params)
            model_type = type(model).__name__

            print(f"   Info for '{version_name}':")
            print(f"  • Model type: {model_type}")
            print(f"  • Total hyperparameters: {n_params}")
            print(f"  • File: {version[version_name]}")
            print(f"  • Size: {file_size:.2f} KB")
            print(f"  • Last Modified: {modified_time}")

            if n_params:
                print(f"\n  • Hyperparameters:")
                for k, v in params.items():
                    print(f"     - {k}: {v}")

        except Exception as e:
            print(f"Error: {e}")
        