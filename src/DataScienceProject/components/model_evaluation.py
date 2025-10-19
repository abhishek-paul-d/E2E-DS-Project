import os 
import pandas as pd
from src.DataScienceProject import logger
from src.DataScienceProject.constants import *
from src.DataScienceProject.utils.common import load_json, save_json,create_directories
from pathlib import Path
from src.DataScienceProject.entity.config_entity import ModelEvaluationConfig
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

import os 
os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/abhishek-paul-d/E2E-DS-Project.mlflow"  
os.environ['MLFLOW_TRACKING_USERNAME']="abhishek-paul-d"
os.environ['MLFLOW_TRACKING_PASSWORD']="8268eeef9b8163ae34f9154fc93810bc6df074cf"


class ModelEvaluation:
    def __init__(self,config=ModelEvaluationConfig):
        self.config=config

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae= mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)
        test_x= test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities=model.predict(test_x)

            (rmse,mae,r2)= self.eval_metrics(test_y,predicted_qualities)

            scores={"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)
            
            model_file = os.path.join("artifacts", "model_evaluation", "model.joblib")
            os.makedirs(os.path.dirname(model_file), exist_ok=True)
            joblib.dump(model, model_file)
            mlflow.log_artifact(model_file, artifact_path="model")

