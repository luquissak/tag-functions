from clients.data_agent_client import DataAgentClient

client = DataAgentClient()

agent = client.get_agent()

print(agent)