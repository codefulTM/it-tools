from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool28(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(28)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 28,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 28")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body">
            <h4>Configuration</h4> 
            <label class="normal-label">Set the global config</label><br>
            <small class="git-code">git config --global user.name "[name]"</small><br>
            <small class="git-code">git config --global user.email "[email]"</small>
            
            <h4>Get started</h4>
            <label class="normal-label">Create a git repository</label><br>
            <small class="git-code">git init</small><br>
            <label class="normal-label">Clone an existing git repository</label><br>
            <small class="git-code">git clone [url]</small>
            
            <h4>I've made a mistake</h4>
            <label class="normal-label">Change last commit message</label><br>
            <small class="git-code">git commit --amend</small><br>
            <label class="normal-label">Undo most recent commit and keep changes</label><br>
            <small class="git-code">git reset HEAD~1</small><br>
            <label class="normal-label">Undo the N most recent commit and keep changes</label><br>
            <small class="git-code">git reset HEAD~N</small><br>
            <label class="normal-label">Undo the N most recent commit and get rid of changes</label><br>
            <small class="git-code">git reset HEAD~N --hard</small><br>
            <label class="normal-label">Reset branch to remote state</label><br>
            <small class="git-code">git fetch origin</small><br>
            <small class="git-code">git reset --hard origin/[branch-name]</small>

            <h4>Miscellaneous</h4>
            <label class="normal-label">Renaming to local master branch to main</label><br>
            <small class="git-code">git branch-m master main</small>
        </div>
        """
    
    def get_js(self):
        return """
            
        """
    
    def get_package(self):
        return ""