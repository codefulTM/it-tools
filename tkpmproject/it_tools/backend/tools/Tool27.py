from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool27(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(27)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 27,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 27")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body">
                <label id="clock" class="chronometer-clock">00:00.000</label>
                <button type="button" id="start-btn" class="normal-btn">Start</button>
                <button hidden type="button" id="stop-btn" class="normal-btn">Stop</button>
                <button type="button" id="reset-btn" class="normal-btn">Reset</button>
            </div>
        """
    
    def get_js(self):
        return """
            const clock = document.getElementById("clock");
            const startButton = document.getElementById("start-btn");
            const stopButton = document.getElementById("stop-btn");
            const resetButton = document.getElementById("reset-btn");

            let startTime = 0;
            let elapsedTime = 0;
            let timerInterval = null;
            let running = false;

            startButton.addEventListener("click", function() {
                startButton.setAttribute("hidden", true);
                stopButton.removeAttribute("hidden");
                start();
            });

            stopButton.addEventListener("click", function() {
                startButton.removeAttribute("hidden");
                stopButton.setAttribute("hidden", true);
                stop();
            });

            resetButton.addEventListener("click", function() {
                startButton.removeAttribute("hidden");
                stopButton.setAttribute("hidden", true);
                reset();
            });

            function timeToString(time) {
                const milliseconds = Math.floor(time % 1000).toString().padStart(3, '0');
                const totalSeconds = Math.floor(time / 1000);
                const minutes = Math.floor(totalSeconds / 60).toString().padStart(2, '0');
                const seconds = (totalSeconds % 60).toString().padStart(2, '0');
                return `${minutes}:${seconds}.${milliseconds}`;
            }

            function updateDisplay() {
                const now = Date.now();
                elapsedTime = now - startTime;
                clock.textContent = timeToString(elapsedTime);
            }

            function start() {
                if (!running) {
                    startTime = Date.now() - elapsedTime;
                    timerInterval = setInterval(updateDisplay, 10);
                    running = true;
                } else {
                    stop();
                }
            }

            function stop() {
                clearInterval(timerInterval);
                running = false;
            }

            function reset() {
                clearInterval(timerInterval);
                startTime = 0;
                elapsedTime = 0;
                running = false;
                clock.textContent = "00:00.000";
            }
        """
    
    def get_package(self):
        return ""