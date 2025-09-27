#global config variable storage
file_char_limit = 10000 #Character limit for files
run_timeout = 30        #timeout for run_python_file
max_iterations = 20     #number of allowed iterations for generate_content loop

#Working directory
working_dir = "./calculator"
#IT IS EXTREMELY IMPORTANT THAT THIS VARIABLE IS SET CORRECTLY 
#TO PREVENT UNWANTED ACCESS OR MODIFICATIONS BY THE AI AGENT

#genai variables
model_name = 'gemini-2.0-flash-001'
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""