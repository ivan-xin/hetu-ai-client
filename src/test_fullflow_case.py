from project.project_api import HetuAIClient
from task.task_api import HetuAITaskClient
from dataset.dataset_api import HetuAIDataGenClient
import json
import os
import time

def test_full_flow():
    """
    Test the complete flow of creating a dataset:
    1. Create a project
    2. Create a task within the project
    3. Generate categories
    4. Generate samples
    5. Save samples
    6. Import samples from a file
    """
    base_url = "http://localhost:8000"
    
    # Initialize clients
    project_client = HetuAIClient(base_url=base_url)
    task_client = HetuAITaskClient(base_url=base_url)
    data_client = HetuAIDataGenClient(base_url=base_url)
    
    print("=== Starting Full Flow Test ===")
    
    # Step 1: Create a project
    print("\n1. Creating a new project...")
    project_name = f"Test_Project_{int(time.time())}"  # Ensure unique project name
    new_project = project_client.create_project(
        name=project_name,
        description="A test project for full flow testing"
    )
    project_id = new_project["id"]
    print(f"Project created: {json.dumps(new_project, indent=2, ensure_ascii=False)}")
    
    # Step 2: Create a task within the project
    print("\n2. Creating a task within the project...")
    task_data = {
        "name": "Full Flow Test Task",
        "description": "Task for testing the full data generation flow",
        "instruction": "Generate AI-related data samples"
    }
    new_task = task_client.create_task(project_id, task_data)
    task_id = new_task["id"]
    print(f"Task created: {json.dumps(new_task, indent=2, ensure_ascii=False)}")
    
    # Step 3: Generate categories
    print("\n3. Generating categories...")
    try:
        categories_input = {
            "node_path": ["root"],
            "num_subtopics": 3,
            "model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "provider": "together_ai",
            "human_guidance": "Generate AI-related categories focusing on applications",
            "drop_unsupported_params": True 
        }
        
        categories_result = data_client.generate_categories(project_id, task_id, categories_input)
        print(f"Categories generated: {json.dumps(categories_result, indent=2, ensure_ascii=False)}")
        
        # Extract a category for sample generation
        topic = "AI Applications"  # Default topic if extraction fails
        if hasattr(categories_result, 'categories') and len(categories_result.categories) > 0:
            topic = categories_result.categories[0]
        
    except Exception as e:
        print(f"Category generation failed: {str(e)}")
        topic = "AI Applications"  # Fallback topic
    
    # Step 4: Generate samples
    print("\n4. Generating samples...")
    try:
        samples_input = {
            "topic": [topic],
            "num_samples": 2,
            "model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "provider": "together_ai",
            "human_guidance": "Generate samples about AI applications in healthcare"
        }
        
        samples_result = data_client.generate_samples(project_id, task_id, samples_input)
        print(f"Samples generated: {json.dumps(samples_result, indent=2, ensure_ascii=False)}")
        
    except Exception as e:
        print(f"Sample generation failed: {str(e)}")
    
    # Step 5: Save individual samples
    print("\n5. Saving individual samples...")
    try:
        sample_data = {
            "input": "What are the applications of AI in medical diagnosis?",
            "topic_path": [topic, "Healthcare"],
            "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "input_provider": "together_ai",
            "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "output_provider": "together_ai",
            "prompt_method": "simple_prompt_builder",
            "human_guidance": "AI applications in medical diagnosis"
        }
        
        save_result = data_client.save_sample(project_id, task_id, sample_data)
        print(f"Sample saved: {json.dumps(save_result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"Saving sample failed: {str(e)}")
    
    # Step 6: Save batch samples
    print("\n6. Saving batch samples...")
    try:
        batch_data = {
            "samples": [
                {
                    "input": "How is AI used in drug discovery?",
                    "topic_path": [topic, "Healthcare", "Drug Discovery"],
                    "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "input_provider": "together_ai",
                    "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "output_provider": "together_ai",
                    "prompt_method": "simple_prompt_builder",
                    "human_guidance": "AI in drug discovery"
                },
                {
                    "input": "What are the ethical considerations of AI in healthcare?",
                    "topic_path": [topic, "Healthcare", "Ethics"],
                    "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "input_provider": "together_ai",
                    "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "output_provider": "together_ai",
                    "prompt_method": "simple_prompt_builder",
                    "human_guidance": "Ethical considerations of AI in healthcare"
                }
            ]
        }
        
        batch_result = data_client.save_samples_batch(project_id, task_id, batch_data)
        print(f"Batch samples saved: {json.dumps(batch_result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"Saving batch samples failed: {str(e)}")
    
    # Step 7: Import samples from file (if file exists)
    print("\n7. Importing samples from file...")
    try:
        # Check if the sample file exists
        temp_file = os.path.abspath("dataset/temp_samples.csv")
        
        if os.path.exists(temp_file):
            request_data = {
                "prompt_method": "simple_prompt_builder",
                "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo"
            }
            
            import_result = data_client.import_samples_from_file(
                project_id, 
                task_id, 
                temp_file,
                request_data
            )
            print(f"File import result: {json.dumps(import_result, indent=2, ensure_ascii=False)}")
        else:
            print(f"Warning: File {temp_file} does not exist, skipping import step")
    except Exception as e:
        print(f"Importing samples from file failed: {str(e)}")
    
    # Optional: Clean up by deleting the project
    # Uncomment if you want to delete the project after testing
    # print("\n8. Cleaning up - deleting project...")
    # try:
    #     delete_result = project_client.delete_project(project_id)
    #     print(f"Project deletion result: {json.dumps(delete_result, indent=2, ensure_ascii=False)}")
    # except Exception as e:
    #     print(f"Project deletion failed: {str(e)}")
    
    print("\n=== Full Flow Test Completed ===")
    print(f"Project ID: {project_id}")
    print(f"Task ID: {task_id}")
    
    return {
        "project_id": project_id,
        "task_id": task_id
    }

if __name__ == "__main__":
    test_full_flow()
