from .nodes import Node_1, Node_2

NODE_CLASS_MAPPINGS = {'Node_1' : Node_1, 'Node_2' : Node_2}

NODE_DISPLAY_NAME_MAPPINGS = {'Node_1' : 'send image to discord', 'Node_2' : 'download file'}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')

for custom_node in NODE_DISPLAY_NAME_MAPPINGS:

    print(f'[ INFO ] | \'{NODE_DISPLAY_NAME_MAPPINGS[custom_node]}\' node loaded.')

print('\n[ INFO ] | All custom nodes loaded.')

print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')
