# Hetu AI Client

Hetu AI Client is a Python client library for interacting with Hetu AI services. The library provides a series of APIs for managing projects, tasks, dataset generation, and model fine-tuning functionalities.

## Directory Structure

```
src/
├── test_project_client.py    # Project management related tests
├── test_task_client.py       # Task management related tests  
├── test_gent_data_client.py  # Data generation related tests
├── test_finetune_client.py   # Model fine-tuning related tests
└── test_dataset.jsonl        # Sample dataset file
```

## File Description

### test_project_client.py
- Demonstrates test cases for project management functionality
- Includes operations like creating projects, getting project lists, getting single projects, updating projects, importing projects, and deleting projects
- Uses HetuAIClient class to implement project management features

### test_task_client.py  
- Demonstrates test cases for task management functionality
- Includes operations like creating tasks, getting task lists, getting single tasks, updating tasks, and deleting tasks
- Uses HetuAITaskClient class to implement task management features

### test_gent_data_client.py
- Demonstrates test cases for data generation functionality
- Includes operations like generating classifications, generating samples, saving single samples, batch saving samples, and importing samples from files
- Uses HetuAIDataGenClient class to implement data generation features

### test_finetune_client.py
- Demonstrates test cases for model fine-tuning functionality
- Includes operations like getting fine-tuning providers, getting hyperparameters, creating dataset splits, getting fine-tuning lists, and creating fine-tuning tasks
- Uses HetuAIFinetuneClient class to implement model fine-tuning features

### test_dataset.jsonl
- Sample dataset file
- Contains multiple AI-related question and answer samples
- Stored in OpenAI Chat format, with each sample including system prompts, user inputs, and assistant responses

## Installation

Install Hetu AI Client using pip:

```bash
pip install -r requirements.txt
```

## Feature Overview

Hetu AI Client provides the following main features:

1. **Project Management**: Create, retrieve, update, and delete projects
2. **Task Management**: Create, retrieve, update, and delete tasks within projects
3. **Dataset Generation**: Generate classifications, samples, save and import datasets
4. **Model Fine-tuning**: Create dataset splits, get fine-tuning providers, create and manage fine-tuning tasks
