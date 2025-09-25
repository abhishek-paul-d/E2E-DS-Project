from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.entity.config_entity import ModelTrainerConfig
from src.DataScienceProject.components.model_trainer import ModelTrainer
from src.DataScienceProject import logger
import pandas as pd

STAGE_NAME="MODEL TRAINER STAGE"

class ModelTrainerPipeline:
    def __init__(self):
       pass

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()
