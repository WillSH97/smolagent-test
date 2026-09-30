import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, GradioUI, LiteLLMModel, MCPClient

from tools import generate_joke, return_random_emoji, get_location

api_key = os.environ.get("GROQ_API_KEY")

mcp_tools = MCPClient(
    [
        {"url": 'https://gateway.mcpservers.org/yahoo-finance/mcp', "transport": "streamable-http"},
        {"url": 'https://destaire.com/mcp', "transport": "streamable-http"}
    ]
)

mcp_tools_list = mcp_tools.get_tools()
# 1. Initialize your model and tools
model = LiteLLMModel(
    model_id="qwen/qwen3.8-27b",  # Or another Groq-supported model ID
    api_base="https://api.groq.com/openai/v1",
    api_key=api_key,
)
tools = [DuckDuckGoSearchTool(), generate_joke, return_random_emoji, get_location]

# 2. Create the CodeAgent
agent = CodeAgent(tools=tools+mcp_tools_list, model=model, add_base_tools=True, )

# 3. Launch the Gradio UI
GradioUI(agent).launch(share=False)


