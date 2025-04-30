from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool21(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(21)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 21,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 21")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body date-generator-container">
                <label class="normal-label-down">Format:</label>
                <select name="date-time-format" class="dropdown" id="date-time-format">
                    <option value="dd/MM/yyyy" selecteed>(Date) dd/MM/yyyy</option>
                    <option value="yyyy/MM/dd">(Date) yyyy/MM/dd</option>
                    <option value="MM/dd/yyyy">(Date) MM/dd/yyyy</option>
                    <option value="hh:mm">(Time) hh:mm</option>
                    <option value="hh:mm:ss">(Time) hh:mm:ss</option>
                    <option value="hh:mm:ss aa">(Time) hh:mm:ss AM/PM</option>
                    <option value="dd/MM/yyyy hh:mm">(Date + Time) dd/MM/yyyy hh:mm</option>
                    <option value="dd/MM/yyyy hh:mm:ss">(Date + Time) dd/MM/yyyy hh:mm:ss</option>
                    <option value="dd/MM/yyyy hh:mm:ss aa">(Date + Time) dd/MM/yyyy hh:mm:ss AM/PM</option>
                    <option value="yyyy/MM/dd hh:mm">(Date + Time) yyyy/MM/dd hh:mm</option>
                    <option value="yyyy/MM/dd hh:mm:ss">(Date + Time) yyyy/MM/dd hh:mm:ss</option>
                    <option value="yyyy/MM/dd hh:mm:ss aa">(Date + Time) yyyy/MM/dd hh:mm:ss AM/PM</option>
                    <option value="MM/dd/yyyy hh:mm">(Date + Time) MM/dd/yyyy hh:mm</option>
                    <option value="MM/dd/yyyy hh:mm:ss">(Date + Time) MM/dd/yyyy hh:mm:ss</option>
                    <option value="MM/dd/yyyy hh:mm:ss aa">(Date + Time) MM/dd/yyyy hh:mm:ss AM/PM</option>
                </select>

                <label class="normal-label">Time zone</label>
                <input type="checkbox" id="time-zone" checked>

                <label class="normal-label-down" id="date-time-output-label">Date/Time:</label>
                <input class="normal-input" type="text" id="date-time-output" readonly>

            </div>

            <span>
                <input type="submit" value="Generate Date" class="normal-btn" id="generate-date">
                <input type="button" value="Copy Date" class="normal-btn" id="copy-date">
            </span>
        """
    
    def get_js(self):
        return """
            const dateTimeFormat = document.getElementById('date-time-format');
            const timeZone = document.getElementById('time-zone');
            const dateTimeOutput = document.getElementById('date-time-output');
            const generateDate = document.getElementById('generate-date');
            const copyDate = document.getElementById('copy-date');

            generateDate.addEventListener('click', () => {
                try {
                    const startDate = new Date(1980, 1, 1);
                    const endDate = new Date(2100, 1, 1);

                    let dateTime = new Date(startDate.getTime() + Math.random() * (endDate.getTime() - startDate.getTime()));
                    let formattedDateTime = '';
                    if (timeZone.checked)
                        formattedDateTime = dateFns.format(dateTime, dateTimeFormat.value + ' (zzz)');
                    else
                        formattedDateTime = dateFns.format(dateTime, dateTimeFormat.value);

                    console.log('Date/Time:', formattedDateTime);
                    dateTimeOutput.value = formattedDateTime;
                } catch (err) {
                    console.error('Failed to generate random date/time', err);
                    alert ('Faild to generate random date/time');
                } 
            });

            copyDate.addEventListener('click', async () => {
                if (!dateTimeOutput || dateTimeOutput.value == '') {
                    alert ('Please generate date/time first!');
                    return;
                }
                try {
                    await navigator.clipboard.writeText(dateTimeOutput.value);
                    alert ('Copied date/time to the clipboard successfully!');
                } catch (err) {
                    console.error('Failed to copy date/time to the clipboard', err);
                    alert ('Failed to copy date/time to the clipboard');
                }
            });
        """
    
    def get_package(self):
        return "https://cdn.jsdelivr.net/npm/date-fns@3.6.0/cdn.min.js"