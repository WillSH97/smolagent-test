from smolagents import InferenceClientModel, CodeAgent, DockerExecutor

docker_executor = DockerExecutor(port=9999)

with CodeAgent(model=InferenceClientModel(), tools=[], python_executor=docker_executor) as agent:
    agent.run("Can you give me the 100th Fibonacci number?")
