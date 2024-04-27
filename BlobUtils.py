from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import shutil
import os

class BlobHandler:
    def __init__(self, dotenv_path='.env', container_name="data-container"):
        """
        Initialize BlobDownloader object.

        Args:
        - local_directory (str): Local directory to save the downloaded files.
        - dotenv_path (str): Path to the .env file containing the Azure Blob Storage connection string. Default is '.env'.
        - container_name (str): Name of the Azure Blob Storage container. Default is "data-container".
        """
        self.dotenv_path = dotenv_path
        self.container_name = container_name

        load_dotenv(self.dotenv_path)
        connection_string = os.getenv('BLOB_STORAGE_CONNECTION_STRING')

        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container=self.container_name)

        # suggested structure:
        # TUM-ai_Makeathon
        # ├── data
        # │   ├── bronze_layer
        # │   │   ├── EuroSAT_MS
        # │   ├── silver_layer
        # │   ├── gold_layer

    def download_blob_folder(self, target_path):
        """
        Downloads files from Azure Blob Storage container to a local directory.

        Args:
        - target_path (str): Path to the local directory to save the downloaded files.
        """
        assert target_path != "", "target_path cannot be empty"
        blob_list = self.container_client.list_blobs()
        blob_folder_path = target_path.replace("data/", "")  # remove the data/ prefix

        for blob in blob_list:
            if not blob.name.startswith(blob_folder_path):
                continue
            # print full paths of the blobs
            blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=blob.name)

            # create folders and subfolders and file
            os.makedirs(os.path.dirname(f"data/{blob.name}"), exist_ok=True)
            with open(f"data/{blob.name}", "wb") as file:
                download_stream = blob_client.download_blob()
                file.write(download_stream.readall())

        print("Download completed.")

    def upload_folder_to_blob(self, source_path):
        """
        Uploads files from a local folder to an Azure Blob Storage container.

        Args:
        - source_path (str): Path to the local folder to be uploaded.
        """
        assert source_path != "", "folder_path cannot be empty"

        # Check if container already exists, if not create it
        if not self.container_client.exists():
            self.container_client.create_container()

        for root, dirs, files in os.walk(source_path):
            if files:
                for file in files:
                    file_path_on_azure = os.path.join(root,file).replace('data/','')
                    file_path_on_local = os.path.join(root,file)
                    # upload the file to blob
                    blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_path_on_azure)
                    with open(file_path_on_local, "rb") as data:
                        blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded completed.")


if __name__ == "__main__":
    # Example usage

    blob_handler = BlobHandler()
    # blob_handler.download_blob_folder(target_path="data/bronze_layer/EuroSAT_MS")
    blob_handler.upload_folder_to_blob(source_path="data/bronze_layer")