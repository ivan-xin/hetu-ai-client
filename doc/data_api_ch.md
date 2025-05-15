
# HetuAI 数据生成 API 文档

## 初始化客户端

```python
from dataset.dataset_api import HetuAIDataGenClient

client = HetuAIDataGenClient(
    base_url="http://localhost:8000",  # API服务的基础URL
    api_key=None  # 可选的API认证密钥
)
```

## API 方法

### 1. 生成分类

生成主题分类树的子分类。

```python
result = client.generate_categories(
    project_id="项目ID",
    task_id="任务ID",
    input_data={
        "node_path": ["root"],  # 父节点路径
        "num_subtopics": 5,  # 要生成的子主题数量
        "model_name": "模型名称",  # 如 "Qwen/Qwen2.5-72B-Instruct-Turbo"
        "provider": "模型提供商",  # 如 "together_ai"
        "human_guidance": "生成指导说明",  # 可选的人工指导
        "drop_unsupported_params": True  # 是否丢弃不支持的参数
    }
)
```

### 2. 生成样本

为指定主题生成样本数据。

```python
result = client.generate_samples(
    project_id="项目ID",
    task_id="任务ID",
    input_data={
        "topic": ["主题路径"],
        "num_samples": 3,  # 要生成的样本数量
        "model_name": "模型名称",
        "provider": "模型提供商",
        "human_guidance": "生成指导说明"
    }
)
```

### 3. 保存单个样本

保存单个生成的样本。

```python
result = client.save_sample(
    project_id="项目ID",
    task_id="任务ID",
    sample_data={
        "input": "样本输入内容",
        "topic_path": "主题路径",
        "input_model_name": "输入模型名称",
        "input_provider": "输入模型提供商",
        "output_model_name": "输出模型名称",
        "output_provider": "输出模型提供商",
        "prompt_method": "提示方法",
        "human_guidance": "人工指导说明"
    },
    session_id="可选的会话ID"
)
```

### 4. 批量保存样本

批量保存多个样本。

```python
result = client.save_samples_batch(
    project_id="项目ID",
    task_id="任务ID",
    batch_data={
        "samples": [
            {
                "input": "样本1输入内容",
                "topic_path": ["主题", "路径"],
                "input_model_name": "输入模型名称",
                "input_provider": "输入模型提供商",
                "output_model_name": "输出模型名称",
                "output_provider": "输出模型提供商",
                "prompt_method": "提示方法",
                "human_guidance": "人工指导说明"
            },
            # 更多样本...
        ]
    }
)
```

### 5. 异步导入样本

异步方式批量导入样本。

```python
result = client.import_samples_async(
    project_id="项目ID",
    task_id="任务ID",
    batch_data={
        "samples": [
            # 样本数据列表，格式同批量保存
        ]
    }
)
```

### 6. 从文件导入样本

从CSV或JSONL文件导入样本。

```python
result = client.import_samples_from_file(
    project_id="项目ID",
    task_id="任务ID",
    file_path="文件路径",  # CSV或JSONL文件
    request_data={
        "prompt_method": "提示方法",
        "input_model_name": "输入模型名称",
        "output_model_name": "输出模型名称",
        "input_provider": "输入模型提供商",
        "output_provider": "输出模型提供商",
        "session_id": "可选的会话ID"
    }
)
```

## 错误处理

所有API方法在遇到错误时会抛出异常，异常信息包含具体的错误详情。建议使用try-except进行错误处理：

```python
try:
    result = client.generate_categories(...)
except Exception as e:
    print(f"操作失败: {str(e)}")
```
