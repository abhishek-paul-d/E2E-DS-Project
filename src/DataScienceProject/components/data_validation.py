import os 
import pandas as pd
from src.DataScienceProject import logger
from src.DataScienceProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config=DataValidationConfig):
        self.config=config

    def validate_data_columns(self)-> bool:
        try:
            validation_status=True
            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()

            for col in all_schema:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                      f.write(f"column : {col} is not in the data")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                      f.write(f"All the columns are present in the data")   

            return validation_status
        except Exception as e:
            raise e