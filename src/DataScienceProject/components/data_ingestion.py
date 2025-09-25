import os 
import urllib.request as request
from src.DataScienceProject import logger
import zipfile
from src.DataScienceProject.entity.config_entity import DataIngestionConfig

class DataIngeston:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self)->str:
       if not os.path.exists(self.config.local_data_file):
           filename, headers= request.urlretrieve(
               url=self.config.source_URL,
               filename= self.config.local_data_file

           )
           logger.info(f"file : {filename} downloaded successfully with following info: {headers}")
       else:
           logger.info("FIle already exists")

    def extract_zip_file(self)->None:
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"extracted all the files to : {unzip_path}")
           
           