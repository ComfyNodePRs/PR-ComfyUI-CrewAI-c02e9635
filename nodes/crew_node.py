from .base_node import BaseNode
from crewai import Crew, Process

class CrewNode(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "tasks": ("TASK", {"default": []}),
            },
            "optional": {
                "topic": ("STRING", {"forceInput": False, "multiline": True,"default": ""}),
                "agents": ("AGENT", {"forceInput": False, "default": []}),
                "process": ("STRING", {"default": "sequential", "choices": ["sequential", "hierarchical"]}),
            },
        }
    INPUT_IS_LIST = (True, True, False, False)
    RETURN_TYPES = ("STRING", "STRING")
    FUNCTION = "create_crew"

    def create_crew(self, tasks, process, topic="", agents=[]):
        # Determine the process type
        process_type = Process.sequential if process[0] == "sequential" else Process.hierarchical

        # Create the Crew instance
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=process_type,
            topic=topic,
        )
        
        # Kick off the process and capture the result
        result = crew.kickoff(inputs={'topic': topic})
        print("\n\n📎Crew AI - result", result)
        return (result, crew.usage_metrics)
    


