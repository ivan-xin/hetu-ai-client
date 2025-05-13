import requests
from typing import Dict, List, Optional, Any

class HetuAITaskClient:
    """
    HetuAI 任务客户端，用于与 hetu_ai_gw 的任务 API 进行交互
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        """
        初始化 HetuAI 任务客户端
        
        Args:
            base_url: API 服务的基础 URL
            api_key: API 认证密钥（如果需要）
        """
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
    
    def create_task(self, project_id: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建新任务
        
        Args:
            project_id: 项目ID
            task_data: 任务数据
            
        Returns:
            创建的任务信息
        """
        url = f"{self.base_url}/api/projects/{project_id}/task"
        
        response = requests.post(url, headers=self.headers, json=task_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"创建任务失败: {error_msg}")
    
    def update_task(self, project_id: str, task_id: str, task_updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新任务信息
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            task_updates: 要更新的字段
            
        Returns:
            更新后的任务信息
        """
        url = f"{self.base_url}/api/projects/{project_id}/task/{task_id}"
        
        response = requests.patch(url, headers=self.headers, json=task_updates)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"更新任务失败: {error_msg}")
    
    def delete_task(self, project_id: str, task_id: str) -> Dict[str, Any]:
        """
        删除任务
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            
        Returns:
            删除操作的结果信息
        """
        url = f"{self.base_url}/api/projects/{project_id}/task/{task_id}"
        
        response = requests.delete(url, headers=self.headers)
        
        if response.status_code == 200:
            return {"success": True, "message": "任务已成功删除"}
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"删除任务失败: {error_msg}")
    
    def get_tasks(self, project_id: str) -> List[Dict[str, Any]]:
        """
        获取项目下的所有任务
        
        Args:
            project_id: 项目ID
            
        Returns:
            任务列表
        """
        url = f"{self.base_url}/api/projects/{project_id}/tasks"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取任务列表失败: {error_msg}")
    
    def get_task(self, project_id: str, task_id: str) -> Dict[str, Any]:
        """
        获取特定任务
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            
        Returns:
            任务信息
        """
        url = f"{self.base_url}/api/projects/{project_id}/tasks/{task_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取任务失败: {error_msg}")
