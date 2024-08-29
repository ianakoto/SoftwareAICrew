import streamlit as st
import re


class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        task_match = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        if task_match:
            task_value = task_match.group(1).strip()
            st.toast(":robot_face: " + task_value)

        for agent, color in zip(['manager', 'frontend_engineer', 'backend_engineer', 'ui_ux_agent'], self.colors):
            if agent in cleaned_data:
                cleaned_data = cleaned_data.replace(agent, f":{color}[{agent}]")

        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            self.color_index = (self.color_index + 1) % len(self.colors)
            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain",
                                                f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
