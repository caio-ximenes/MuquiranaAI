from langchain.agents import create_agent


agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    system_prompt="You are a finance consultor"
)

