# Wine-Quality---ML-Project-with-MLFlow


## WorkFlows:

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update app.py

**template.py** file to create files and folders using Python script. __init__.py is initialized to make the local package and import the objects.
 * .github folder is created to deploy the CI?CD Pipeline. As the .github folder can't commit without having a file, therefore .gitkeep file is created within it.
 * config.yaml/config - to make all the configurations related to this project.
 * requirements.txt - install required libraries for this project.
     * python-box to make all the configuration tasks easy to organize and neatly write code.
     * pyYAML - to deal with yaml files.
     * ensure==1.0.2
     * joblib
     * types-PyYAML
     * -e . look for the setup.py file.
 * setup.py stores local package information.

MLFLOW_TRACKING_URI=https://dagshub.com/Kavyagandhi23/Wine-Quality---ML-Project-with-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=Kavyagandhi23 \
MLFLOW_TRACKING_PASSWORD="******" \
python script.py


