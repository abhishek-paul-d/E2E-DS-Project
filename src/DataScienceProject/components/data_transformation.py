import os 
import pandas as pd
from src.DataScienceProject import logger
from src.DataScienceProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self,config=DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
       data=pd.read_csv(self.config.data_path)
       train,test=train_test_split(data,test_size=0.2,random_state=42)
       train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
       test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

       logger.info("Split the data into train and test successfully")
       logger.info(f"train data : {train.shape} and test data : {test.shape}")

       print(train.shape)
       print(test.shape)
