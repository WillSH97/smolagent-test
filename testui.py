import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, GradioUI, LiteLLMModel

api_key = os.environ.get("GROQ_API_KEY")

# 1. Initialize your model and tools
model = LiteLLMModel(
    model_id="qwen/qwen3.8-27b",  # Or another Groq-supported model ID
    api_base="https://api.groq.com/openai/v1",
    api_key=api_key,
)
tools = [DuckDuckGoSearchTool()]

# 2. Create the CodeAgent
agent = CodeAgent(tools=tools, model=model)

# 3. Launch the Gradio UI
GradioUI(agent).launch(share=False)
