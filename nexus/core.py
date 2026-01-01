import uuid
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class Message(BaseModel):
    id: str = str(uuid.uuid4())
    sender: str
    content: str
    timestamp: str

class AgentConfig(BaseModel):
    name: str
    role: str
    system_prompt: str
    tools: List[str] = []

class Agent:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.memory: List[Message] = []

    def receive_message(self, message: Message):
        self.memory.append(message)

    def think(self, context: str) -> str:
        # Placeholder for LLM call
        # In a real implementation, this would call Ollama or OpenAI
        return f"[{self.config.name}]: I have processed the request based on my role as {self.config.role}. {context[:50]}..."

class NexusOrchestrator:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.logs: List[str] = []

    def register_agent(self, agent: Agent):
        self.agents[agent.config.name] = agent
        self.logs.append(f"Registered agent: {agent.config.name}")

    def broadcast(self, sender_name: str, content: str):
        msg = Message(sender=sender_name, content=content, timestamp="now")
        for name, agent in self.agents.items():
            if name != sender_name:
                agent.receive_message(msg)
        self.logs.append(f"Broadcast from {sender_name}: {content}")

    def run_swarm(self, task: str):
        # Simple round-robin or sequence logic for demo
        results = []
        self.broadcast("User", task)
        
        for name, agent in self.agents.items():
            response = agent.think(task)
            results.append(response)
            self.broadcast(name, response)
            
        return results
