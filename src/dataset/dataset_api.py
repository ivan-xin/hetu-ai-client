import requests
from typing import Dict, List, Optional, Any

class HetuAIDataGenClient:
    """
    HetuAI 数据生成客户端，用于与 hetu_ai_gw 的数据生成 API 进行交互
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        """
        初始化 HetuAI 数据生成客户端
        
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
    
    def generate_categories(
        self, 
        project_id: str, 
        task_id: str, 
        input_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        生成分类
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            input_data: 输入数据，包含 node_path, num_subtopics, model_name, provider 等
            
        Returns:
            生成的分类信息
        """
        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/generate_categories"
        
        response = requests.post(url, headers=self.headers, json=input_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"生成分类失败: {error_msg}")
    
    def generate_samples(
        self, 
        project_id: str, 
        task_id: str, 
        input_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        生成样本
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            input_data: 输入数据，包含 topic, num_samples, model_name, provider 等
            
        Returns:
            生成的样本信息
        """
        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/generate_samples"
        
        response = requests.post(url, headers=self.headers, json=input_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"生成样本失败: {error_msg}")
    
    def save_sample(
        self, 
        project_id: str, 
        task_id: str, 
        sample_data: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        保存样本
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            sample_data: 样本数据
            session_id: 会话ID（可选）
            
        Returns:
            保存的样本信息
        """
        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/save_sample"
        params = {}
        if session_id:
            params["session_id"] = session_id
        
        response = requests.post(url, headers=self.headers, json=sample_data, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"保存样本失败: {error_msg}")
    
    def save_samples_batch(
        self, 
        project_id: str, 
        task_id: str, 
        batch_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        批量保存样本
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            batch_data: 批量样本数据
            
        Returns:
            保存的样本信息列表
        """
        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/save_samples_batch"
        
        response = requests.post(url, headers=self.headers, json=batch_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"批量保存样本失败: {error_msg}")
    
    def import_samples_async(
        self, 
        project_id: str, 
        task_id: str, 
        batch_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        异步导入样本
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            batch_data: 批量样本数据
            
        Returns:
            导入操作的状态信息
        """
        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/import_samples_async"
        
        response = requests.post(url, headers=self.headers, json=batch_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = response.json().get("detail", "Unknown error")
            raise Exception(f"异步导入样本失败: {error_msg}")
    
    def import_samples_from_file(
        self, 
        project_id: str, 
        task_id: str, 
        file_path: str,
        request_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        从文件导入样本
        
        Args:
            project_id: 项目ID
            task_id: 任务ID
            file_path: 文件路径
            request_data: 请求数据（可选）
            
        Returns:
            导入操作的状态信息
        """

        if request_data is None:
            request_data = {}
        
        # 确保prompt_method在查询参数中
        params = {
            "prompt_method": request_data.get("prompt_method", "simple_prompt_builder"),
            "input_model_name": request_data.get("input_model_name", ""),
            "output_model_name": request_data.get("output_model_name", ""),
            "input_provider": request_data.get("input_provider", ""),
            "output_provider": request_data.get("output_provider", ""),
            "session_id": request_data.get("session_id", "")
        }
        
        # 准备文件上传
        # files = {"file": open(file_path, "rb")}

        files = {"file": open(file_path, "rb")}

        url = f"{self.base_url}/api/dataset/projects/{project_id}/tasks/{task_id}/import_samples_from_file"
        

        try:
            print("\n测试从文件导入样本SUCCESS000")
            response = requests.post(url, params=params, files=files)
            response.raise_for_status()
            print("\n测试从文件导入样本SUCCESS")
            return response.json()
        
        except Exception as e:
            raise Exception(f"从文件导入样本失败: {str(e)}")
        finally:
            # 确保关闭文件
            for f in files.values():
                f.close()
