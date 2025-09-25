from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.entity.config_entity import DataTransformationConfig
from src.DataScienceProject.components.data_transformation import DataTransformation
from src.DataScienceProject import logger
import pandas as pd


STAGE_NAME="Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self,config=DataTransformationConfig):
       pass

    def initiate_data_transformation(self):
        try:
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_splitting()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        