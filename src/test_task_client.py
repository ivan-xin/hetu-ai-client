from task.task_api import HetuAITaskClient
import json

def main():
    # 初始化客户端
    client = HetuAITaskClient(base_url="http://localhost:8000")
    
    # 测试参数
    project_id = "250615285993"
    
    # 测试创建任务
    print("测试创建任务...")
    task_data = {
        "name": "Test Task 11",
        "description": "This is a test task",
        "instruction": "This is a test instruction",
    }
    
    try:
        new_task = client.create_task(project_id, task_data)
        print(f"创建的任务: {json.dumps(new_task, indent=2, ensure_ascii=False)}")
        
        # 获取任务ID
        # task_id = new_task["id"]
        
        # 测试获取所有任务
        # print("\n测试获取所有任务...")
        # tasks = client.get_tasks(project_id)
        # print(f"所有任务: {json.dumps(tasks, indent=2, ensure_ascii=False)}")
        
        # # 测试获取特定任务
        # print(f"\n测试获取任务 {task_id}...")
        # task = client.get_task(project_id, task_id)
        # print(f"任务详情: {json.dumps(task, indent=2, ensure_ascii=False)}")
        
        # # 测试更新任务
        # print(f"\n测试更新任务 {task_id}...")
        # task_updates =  {"name": "Updated Task"}
        # updated_task = client.update_task(project_id, task_id, task_updates)
        # print(f"更新后的任务: {json.dumps(updated_task, indent=2, ensure_ascii=False)}")
        
        # 测试删除任务
        # print(f"\n测试删除任务 {task_id}...")
        # delete_result = client.delete_task(project_id, task_id)
        # print(f"删除结果: {json.dumps(delete_result, indent=2, ensure_ascii=False)}")
        
    except Exception as e:
        print(f"操作失败: {str(e)}")
    
    print("\n所有测试完成!")

if __name__ == "__main__":
    main()
