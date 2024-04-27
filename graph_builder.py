from osgeo import gdal
from datetime import datetime
import os
from utils.meta_data_extraction import parse_date_from_filename, format_datetime, parse_group_from_filename, return_azure_file_path
from knowledge_graph.knowledge_graph import KnowledgeGraph

KG = KnowledgeGraph()

path = os.path.join(os.getcwd(), "silver_layer/SEN4AMA")

for root, dirs, files in os.walk(path):
    
    for file in files:
        
        if not file.startswith('.') and file.split("_")[1].isdigit():
            dataset = gdal.Open(os.path.join(root, file))
            file_path = os.path.join(root, file)
        
            image_data_dict = {
                'date': format_datetime(parse_date_from_filename(file)),
                'file_name': os.path.basename(file_path),
                'group': parse_group_from_filename(file),
                'file_path': os.path.join(root, file), 
                'azure_file_path': return_azure_file_path(file_path),
                'coordinate_system_(projection)': dataset.GetProjection(),
                'geotransform': dataset.GetGeoTransform(),
            }
            
            KG.add_image_as_node(image_data_dict)
            dataset = None
            #processed += 1
            #if processed >= 10:
            #    break

    #if processed >= 10:
    #    break


graph_path = os.path.join(os.getcwd(), "gold_layer", "SEN4AMA.rpty")
KG.save_graph(graph_path)

