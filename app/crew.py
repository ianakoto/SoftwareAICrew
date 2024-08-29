import os

from utils import get_openai_api_key, get_serper_api_key
from utils import init_langtrace_api_key

init_langtrace_api_key()

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import CodeDocsSearchTool
from crewai_tools import WebsiteSearchTool
from langchain_openai import ChatOpenAI


@CrewBase
class SoftwareEngineeringCrew:
    """SoftwareEngineering crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    openai_api_key = get_openai_api_key()
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"
    os.environ["SERPER_API_KEY"] = get_serper_api_key()

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo",
                              temperature=0.7)

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            tools=[SerperDevTool(),
                   WebsiteSearchTool()],
            verbose=os.environ["DEBUG"]
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            llm=self.llm,
            tools=[SerperDevTool(),
                   CodeDocsSearchTool()],
            verbose=os.environ["DEBUG"]
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            llm=self.llm,
            tools=[SerperDevTool(),
                   CodeDocsSearchTool()],
            verbose=os.environ["DEBUG"]
        )


    @agent
    def ui_ux_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ui_ux_agent'],
            llm=self.llm,
            tools=[SerperDevTool(),
                   WebsiteSearchTool()],
            verbose=os.environ["DEBUG"]
        )


    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            llm=self.llm,
            verbose=os.environ["DEBUG"]
        )

    @task
    def idea_expansion_task(self) -> Task:
        return Task(
            config=self.tasks_config['idea_expansion_task']
        )

    @task
    def ui_ux_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['ui_ux_search_task']
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task']
        )

    @task
    def backend_task(self) -> Task:
        return Task(
            config=self.tasks_config['backend_task']
        )

    @task
    def writer_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_agent_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SoftwareEngineering crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            manager_llm=self.llm,
            process=Process.hierarchical,
            verbose=os.environ["DEBUG"],
        )
