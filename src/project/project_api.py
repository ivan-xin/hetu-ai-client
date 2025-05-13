import requests
from typing import Dict, List, Optional, Any
import json

class HetuAIClient:
    """
    HetuAI 客户端，用于与 hetu_ai_gw 的项目 API 进行交互
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        """
        初始化 HetuAI 客户端
        
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
    
    def create_project(self, name: str, description: str = "") -> Dict[str, Any]:
        """
        创建新项目
        
        Args:
            name: 项目名称
            description: 项目描述
            
        Returns:
            创建的项目信息
        """
        url = f"{self.base_url}/api/project"
        payload = {
            "name": name,
            "description": description
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"创建项目失败: {error_msg}")
    
    def get_projects(self) -> List[Dict[str, Any]]:
        """
        获取所有项目
        
        Returns:
            项目列表
        """
        url = f"{self.base_url}/api/projects"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json().get("projects", [])
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取项目列表失败: {error_msg}")
    
    def get_project(self, project_id: str) -> Dict[str, Any]:
        """
        获取特定项目
        
        Args:
            project_id: 项目ID
            
        Returns:
            项目信息
        """
        url = f"{self.base_url}/api/projects/{project_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取项目失败: {error_msg}")
    
    def update_project(self, project_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新项目信息
        
        Args:
            project_id: 项目ID
            updates: 要更新的字段，可以包含 name 和/或 description
            
        Returns:
            更新后的项目信息
        """
        url = f"{self.base_url}/api/projects/{project_id}"
        
        response = requests.patch(url, headers=self.headers, json=updates)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"更新项目失败: {error_msg}")
    
    def delete_project(self, project_id: str) -> Dict[str, Any]:
        """
        删除项目
        
        Args:
            project_id: 项目ID
            
        Returns:
            删除操作的结果信息
        """
        url = f"{self.base_url}/api/projects/{project_id}"
        
        response = requests.delete(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"删除项目失败: {error_msg}")
    
    def import_project(self, project_path: str) -> Dict[str, Any]:
        """
        导入现有项目
        
        Args:
            project_path: 项目路径
            
        Returns:
            导入的项目信息
        """
        url = f"{self.base_url}/api/import-project"
        payload = {
            "project_path": project_path
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"导入项目失败: {error_msg}")
