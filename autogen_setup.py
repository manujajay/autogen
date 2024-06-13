import os
import json
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

def load_config_list(file_path):
    with open(file_path, 'r') as file:
        config_list = json.load(file)
    for config in config_list:
        if 'api_key' in config and config['api_key'] == '${OPENAI_API_KEY}':
            config['api_key'] = os.getenv("OPENAI_API_KEY")
    return config_list

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Load configuration from file
config_list = load_config_list("OAI_CONFIG_LIST.json")

# Initialize Assistant and UserProxy agents
llm_config = {
    "config_list": config_list
}

# Create the assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

# Initialize UserProxyAgent
code_executor = LocalCommandLineCodeExecutor(work_dir="coding")
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"executor": code_executor}
)

# Print statements for verification
print("Assistant Agent Configuration:", assistant)
print("User Proxy Agent Configuration:", user_proxy)

# Start a conversation
user_proxy.initiate_chat(assistant, message="Hello, AutoGen!")
