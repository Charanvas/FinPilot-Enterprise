from app.agents.supervisor_agent import SupervisorAgent

agent = SupervisorAgent()

result = agent.process(
    file_path="uploads/invoice.pdf",
    expected_amount=400,
)

print(result.model_dump())