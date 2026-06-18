from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


# define the class for our crew
@CrewBase
class StoryCrew():
    
    agents: list[BaseAgent]
    tasks: list[Task]
    
    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # ============= Agents ====================
    @agent
    def story_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["story_planner"]
        )
        
    @agent
    def story_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["story_writer"]
        )
    
    @agent
    def story_editor(self) -> Agent:
        return Agent(
            config=self.agents_config["story_editor"]
        )
        
    # ============== Tasks ===========================
    # order of task definition matters
    @task
    def story_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["story_planning_task"]
        )
        
    @task
    def story_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["story_writing_task"],
        )
    
    @task
    def story_editing_task(self) -> Task:
        return Task(
            config=self.tasks_config["story_editing_task"],
            output_file="story/story.md"
        )
        
    # ================ Crew ===============================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )