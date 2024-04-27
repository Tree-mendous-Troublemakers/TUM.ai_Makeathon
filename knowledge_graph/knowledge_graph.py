from raphtory import Graph
import os

class KnowledgeGraph:
    def __init__(self):
        self.graph = Graph()
            
    def graph_exists(self, path):  
        """
        Check if the graph file exists at the specified path.
        """
        return os.path.exists(path)
                    
    def save_graph(self, path):
        self.graph.save_to_file(path)
        
    def add_node(self, timestamp, id, properties=None):
        self.graph.add_node(timestamp=timestamp, id=id, properties=properties)

    def add_image_as_node(self, image_data_dict):       
        self.graph.add_node(
            timestamp=image_data_dict['date'],
            id=image_data_dict['file_name'],
            properties={
            "group": image_data_dict['group'],
            "file_path": image_data_dict['file_path'],
            "azure_file_path": image_data_dict['azure_file_path'],
            "coordinate_system_(projection)": image_data_dict['coordinate_system_(projection)'],
            'geotransform': image_data_dict['geotransform'],
            }
        )

    def remove_node(self, timestamp, id):
        self.graph.remove_node(timestamp=timestamp, id=id)

    def add_edge(self, timestamp, src, dst, properties=None):
        self.graph.add_edge(timestamp=timestamp, src=src, dst=dst, properties=properties)

    def remove_edge(self, timestamp, src, dst):
        self.graph.remove_edge(timestamp=timestamp, src=src, dst=dst)

    def has_node(self, id):
        return self.graph.has_node(id)
    
    def has_edge(self, src, dst):
        return self.graph.has_edge(src=src, dst=dst)

    def load_graph(self, path):
        if os.path.isdir(path):

            pass
        else:
            # Loading from a file
            self.graph = Graph.load_from_file(path)

    def get_node(self, id):
        return self.graph.vertex(id)

    def get_nodes(self):
        return self.graph.nodes
    
    def get_edges(self):
        return self.graph.edges

    def get_edge(self, src, dst):
        return self.graph.edge(src, dst)
    
