# This is used so we can reference the python packages created in other CRISPDM steps

import sys
sys.path.append("..")

class {{cookiecutter.model_class}}:

    ###
    ### This method is the entry point for doing a prediction.  
    def predict(self, data: dict) -> dict:
        # Clean # prepare data
        self.prepare_data(data)

        # Prediction logic here

    def prepare_data(self, data):
        pass
        # Data preparation logic here
