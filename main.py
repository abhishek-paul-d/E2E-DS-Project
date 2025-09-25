def main():
    print("Hello from data-science!")


if __name__ == "__main__":
    main()


from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.DataScienceProject.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Validation Stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

