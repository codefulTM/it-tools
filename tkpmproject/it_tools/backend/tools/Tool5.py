
from backend.classes.ToolComponent import ToolComponent

class Tool5(ToolComponent):
    def get_info(self):
        return {
            'id': 5,
            'name': 'Text To Unicode',
            'description': 'A converter that converts text to unicode.',
            'category': 'Convr',
            'is_premium': False,
            'is_enabled': True
        }

    def get_html(self):
        return """"""

    def get_js(self):
        return """"""
        