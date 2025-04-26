class Tool:
    def __init__(self, id, name, description, category, is_premium, is_enabled):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.is_premium = is_premium
        self.is_enabled = is_enabled

    def get_html(self):
        return None
    
    def get_js(self):
        return None