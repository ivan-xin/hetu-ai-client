from project.project_api import HetuAIClient
import json

#!!!!! 1，输入内容时英文
#!!!!! 2，创建项目时，项目名字需要是唯一的

def main():
    # 初始化客户端
    client = HetuAIClient(base_url="http://localhost:8000")
    
    # 测试创建项目
    print("测试创建项目...")
    new_project = client.create_project(
        name="finetune test 01", 
        description="This is a project for testing"
    )
    print(f"创建的项目: {json.dumps(new_project, indent=2, ensure_ascii=False)}")
    
    # 获取项目ID
    project_id = new_project["id"]
    project_id = "303941345314"
    # 测试获取所有项目
    print("\n测试获取所有项目...")
    projects = client.get_projects()
    print(f"所有项目: {json.dumps(projects, indent=2, ensure_ascii=False)}")
    


    # 测试获取特定项目
    print(f"\n测试获取项目 {project_id}...")
    project = client.get_project(project_id)
    print(f"项目详情: {json.dumps(project, indent=2, ensure_ascii=False)}")
    

    # 测试更新项目
    print(f"\n测试更新项目 {project_id}...")
    updated_project = client.update_project(
        project_id=project_id,
        updates={"name": "Updated test items", "description": "This is an updated test project description"}
    )
    print(f"更新后的项目: {json.dumps(updated_project, indent=2, ensure_ascii=False)}")
    

    # 测试导入项目
    # print("\n测试导入项目...")
    # try:
    #     imported_project = client.import_project("/path/to/existing/project")
    #     print(f"导入的项目: {json.dumps(imported_project, indent=2, ensure_ascii=False)}")
    # except Exception as e:
    #     print(f"导入项目失败: {str(e)}")
    


    # # 测试删除项目
    print(f"\n测试删除项目 {project_id}...")
    delete_result = client.delete_project(project_id)
    print(f"删除结果: {json.dumps(delete_result, indent=2, ensure_ascii=False)}")
    
    print("\n所有测试完成!")

if __name__ == "__main__":
    main()
