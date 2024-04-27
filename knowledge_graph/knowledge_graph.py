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
        """
        Save the graph to the specified path.
        """
        try:
            abs_path = os.path.abspath(path)
            print('🟢 Graph was saved to path: '+ abs_path)
            self.graph.save_to_file(abs_path)
        except Exception as e:
            print(f"Error saving graph: {e}")

    def get_property(self, key):
        return self.graph.properties.get(key)

    def add_node(self, timestamp, id, properties=None):
        self.graph.add_node(timestamp=timestamp, id=id, properties=properties)

    def add_image_as_node(self, issue_dict):       
        if 'embedding_target' in issue_dict:

            self.graph.add_node(
                timestamp=issue_dict['created'],
                id=issue_dict['key'],
                properties={
                "type": issue_dict['type'],
                "summary": issue_dict['summary'],
                "description": issue_dict['description'],
                "parent": str(issue_dict['parent']),
                "status": issue_dict['status'],
                "priority": issue_dict['priority'],
                "created": issue_dict['created'],
                "updated": issue_dict['updated'],
                "assignee": issue_dict['assignee'],
                "reporter": issue_dict['reporter'],
                "issuelinks": str(issue_dict['issuelinks']),
                "embedding_target": issue_dict.get('embedding_target'), # for details on embedding_target see nlp_utils.py module.
                "embedding": issue_dict.get('embedding')
                } 
            )

        else: 
            self.graph.add_node(
                timestamp=issue_dict['created'],
                id=issue_dict['key'],
                properties={
                "type": issue_dict['type'],
                "summary": issue_dict['summary'],
                "description": issue_dict['description'],
                "parent": str(issue_dict['parent']),
                "status": issue_dict['status'],
                "priority": issue_dict['priority'],
                "created": issue_dict['created'],
                "updated": issue_dict['updated'],
                "assignee": issue_dict['assignee'],
                "reporter": issue_dict['reporter'],
                "issuelinks": str(issue_dict['issuelinks'])
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
    
    def get_vertices(self):
        return self.graph.vertices

    def get_edge(self, src, dst):
        return self.graph.edge(src, dst)
    
    def get_edges(self):
        return self.graph.edges

