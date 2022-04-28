import os
from click import command
from dotenv import load_dotenv
from subprocess import Popen

load_dotenv()
my_env = os.environ.copy()
my_env["HF_SPACE"] = "embed/Housto/ToonifyApp"

command = ["mercury", "run", f"0.0.0.0:{os.environ.get('PORT', 7860)}"]
print(command)

worker = Popen(command, env = my_env)
worker.wait()