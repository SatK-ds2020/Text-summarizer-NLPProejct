import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

# Define project root directory
project_name = 'Text-Summarizer'

# # Set up logging directory

# log_dir = Path(os.path.join(project_name, 'logs'))
# log_dir.mkdir(parents=True, exist_ok=True)

# log_file = Path(os.path.join(log_dir, 'text_summarizer.log'))

# # Create logger

# logger = logging.getLogger('text_summarizer')
# logger.basicConfig(level=logging.INFO,format='%(asctime)s: %(levelname)s: %(message)s]: %(name)s: %(lineno)s')

# # Create file handler

# fh = logging.FileHandler(log_file)
# fh.setLevel(logging.INFO)

# # Create console handler

# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)

# # Add handlers to logger

# logger.addHandler(fh)
# logger.addHandler(ch)

# logger.info('Project initialized')
# logger.info(f'Project name: {project_name}')

# Create directories for data and output    

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    file_path = Path(file)
    filedir, filename=os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {file_path.parent} for the file {filename}')
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'Created empty file: {file_path}')

    else:
        logging.info(f'File {file_path} already exists and is not empty')
