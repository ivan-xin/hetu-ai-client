import requests
from typing import Dict, List, Optional, Any

class HetuAIFinetuneClient:
    """
    HetuAI 微调客户端，用于与 hetu_ai_gw 的微调 API 进行交互
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        """
        初始化 HetuAI 微调客户端
        
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
    
    def get_dataset_splits(self, project_id: str, task_id: str) -> List[Dict[str, Any]]:
        """
        获取数据集分割列表
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            
        Returns:
            数据集分割列表
        """
        url = f"{self.base_url}/api/finetune/projects/{project_id}/tasks/{task_id}/dataset_splits"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取数据集分割失败: {error_msg}")
    
    def get_finetunes(self, project_id: str, task_id: str, update_status: bool = False) -> List[Dict[str, Any]]:
        """
        获取微调列表
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            update_status: 是否更新状态
            
        Returns:
            微调列表
        """
        url = f"{self.base_url}/api/finetune/projects/{project_id}/tasks/{task_id}/finetunes"
        params = {"update_status": str(update_status).lower()}
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取微调列表失败: {error_msg}")
    
    def get_finetune(self, project_id: str, task_id: str, finetune_id: str) -> Dict[str, Any]:
        """
        获取特定微调
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            finetune_id: 微调ID
            
        Returns:
            微调信息
        """
        url = f"{self.base_url}/api/finetune/projects/{project_id}/tasks/{task_id}/finetunes/{finetune_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取微调失败: {error_msg}")
    
    def update_finetune(self, project_id: str, task_id: str, finetune_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新微调信息
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            finetune_id: 微调ID
            updates: 要更新的字段
            
        Returns:
            更新后的微调信息
        """
        url = f"{self.base_url}/api/projects/{project_id}/tasks/{task_id}/finetunes/{finetune_id}"
        
        response = requests.patch(url, headers=self.headers, json=updates)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"更新微调失败: {error_msg}")
    
    def get_finetune_providers(self) -> List[Dict[str, Any]]:
        """
        获取微调提供商列表
        
        Returns:
            微调提供商列表
        """
        url = f"{self.base_url}/api/finetune/finetune_providers"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取微调提供商失败: {error_msg}")
    
    def get_finetune_hyperparameters(self, provider_id: str) -> List[Dict[str, Any]]:
        """
        获取微调超参数
        
        Args:
            provider_id: 提供商ID
            
        Returns:
            超参数列表
        """
        url = f"{self.base_url}/api/finetune/hyperparameters/{provider_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"获取微调超参数失败: {error_msg}")
    
    def create_dataset_split(self, project_id: str, task_id: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建数据集分割
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            request_data: 请求数据
            
        Returns:
            创建的数据集分割
        """
        url = f"{self.base_url}/api/finetune/projects/{project_id}/tasks/{task_id}/dataset_splits"
        
        response = requests.post(url, headers=self.headers, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"创建数据集分割失败: {error_msg}")
    
    def create_finetune(self, project_id: str, task_id: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建微调
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            request_data: 请求数据
            
        Returns:
            创建的微调
        """
        url = f"{self.base_url}/api/finetune/projects/{project_id}/tasks/{task_id}/finetunes"
        
        response = requests.post(url, headers=self.headers, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"创建微调失败: {error_msg}")
    
    def download_dataset_jsonl(
        self, 
        project_id: str, 
        task_id: str, 
        dataset_id: str, 
        split_name: str, 
        format_type: str, 
        data_strategy: str,
        system_message_generator: Optional[str] = None,
        custom_system_message: Optional[str] = None,
        custom_thinking_instructions: Optional[str] = None
    ) -> bytes:
        """
        下载数据集 JSONL
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            dataset_id: 数据集ID
            split_name: 分割名称
            format_type: 格式类型
            data_strategy: 数据策略
            system_message_generator: 系统消息生成器
            custom_system_message: 自定义系统消息
            custom_thinking_instructions: 自定义思考指令
            
        Returns:
            JSONL 文件内容
        """
        url = f"{self.base_url}/api/download_dataset_jsonl"
        params = {
            "project_id": project_id,
            "task_id": task_id,
            "dataset_id": dataset_id,
            "split_name": split_name,
            "format_type": format_type,
            "data_strategy": data_strategy
        }
        
        if system_message_generator:
            params["system_message_generator"] = system_message_generator
        if custom_system_message:
            params["custom_system_message"] = custom_system_message
        if custom_thinking_instructions:
            params["custom_thinking_instructions"] = custom_thinking_instructions
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.content
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"下载数据集失败: {error_msg}")
