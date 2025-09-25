from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.entity.config_entity import DataValidationConfig
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger
import pandas as pd


STAGE_NAME="Data Validation Stage"

class DataValidationPipeline:
    def __init__(self,config=DataValidationConfig):
       pass

    def initiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        validation_status=data_validation.validate_data_columns()
        if validation_status:
            logger.info("Data Validation is completed and all the columns are present in the data")
        else:
            logger.info("Data Validation is completed and some columns are missing in the data")

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e