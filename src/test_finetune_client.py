from finetune.test_finetune_api import HetuAIFinetuneClient
import json
import os

def main():
    # 初始化客户端
    client = HetuAIFinetuneClient(base_url="http://localhost:8000")
    
    # 测试参数
    project_id = "250615285993"
    task_id = "316831576302"
    
    #测试获取微调提供商
    # print("测试获取微调提供商...")
    # try:
    #     providers = client.get_finetune_providers()
    #     print(f"微调提供商: {json.dumps(providers, indent=2, ensure_ascii=False)}")
        
    #     if providers:
    #         provider_id = providers[2]["id"]
            
    #         # 测试获取超参数
    #         print(f"\n测试获取提供商 {provider_id} 的超参数...")
    #         hyperparameters = client.get_finetune_hyperparameters(provider_id)
    #         print(f"超参数: {json.dumps(hyperparameters, indent=2, ensure_ascii=False)}")
    # except Exception as e:
    #     print(f"获取微调提供商或超参数失败: {str(e)}")


    # 测试获取数据集分割
    # print("\n测试获取数据集分割...")
    # try:
    #     dataset_splits = client.get_dataset_splits(project_id, task_id)
    #     print(f"数据集分割: {json.dumps(dataset_splits, indent=2, ensure_ascii=False)}")
    # except Exception as e:
    #     print(f"获取数据集分割失败: {str(e)}")
    
    # 测试创建数据集分割
    # print("\n测试创建数据集分割...")
    # try:
    #     split_data = {
    #         "name": "Test Split 2",
    #         "dataset_split_type": "train_test",
    #         "filter_id": "all",
    #         "description": "Test description",
    #     }
    #     dataset_split = client.create_dataset_split(project_id, task_id, split_data)
    #     print(f"创建的数据集分割: {json.dumps(dataset_split, indent=2, ensure_ascii=False)}")
        
    #     # 获取数据集分割ID
    #     dataset_split_id = dataset_split["id"]
    # except Exception as e:
    #     print(f"创建数据集分割失败: {str(e)}")
    #     dataset_split_id = "default_split_id"  # 使用默认值继续测试
    
    #     # 测试获取微调列表
    # print("\n测试获取微调列表...")
    # try:
    #     finetunes = client.get_finetunes(project_id, task_id)
    #     print(f"微调列表: {json.dumps(finetunes, indent=2, ensure_ascii=False)}")
    # except Exception as e:
    #     print(f"获取微调列表失败: {str(e)}")

    # # 测试创建微调
    # print("\n测试创建微调...")
    try:
        # finetune_data = {
        #     "name": "test_finetune",
        #     "description": "Test description",
        #     "dataset_id": dataset_split_id,
        #     "train_split_name": "train",
        #     # "validation_split_name": "test",
        #     "parameters": {"learning_rate": 0.001, "epochs": 10},
        #     "provider": "together_ai",
        #     "base_model_id": "Qwen/Qwen3-14B",
        #     "custom_system_message": "Test system message",
        #     "custom_thinking_instructions": "Think step by step, explaining your reasoning.",
        #     "data_strategy": "final_only",
        # }
        # finetune = client.create_finetune(project_id, task_id, finetune_data)
        # print(f"创建的微调: {json.dumps(finetune, indent=2, ensure_ascii=False)}")
        
        # 获取微调ID
        finetune_id = 218510169618 #finetune["id"]
        
        # 测试获取特定微调
        print(f"\n测试获取微调 {finetune_id}...")
        finetune_detail = client.get_finetune(project_id, task_id, finetune_id)
        print(f"微调详情: {json.dumps(finetune_detail, indent=2, ensure_ascii=False)}")
        
        # 测试更新微调
        # print(f"\n测试更新微调 {finetune_id}...")
        # update_data = {
        #     "name": "updated_test_finetune",
        #     "description": "Updated description"
        # }
        # updated_finetune = client.update_finetune(project_id, task_id, finetune_id, update_data)
        # print(f"更新后的微调: {json.dumps(updated_finetune, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"微调操作失败: {str(e)}")

        # 测试下载数据集
    print("\n测试下载数据集 JSONL...")
    try:
        dataset_id = "768030305703"
        split_name = "train"
        format_type = "openai_chat_jsonl"
        data_strategy = "final_only"
        custom_system_message = "your are a ai teacher"
        custom_thinking_instructions = "Think step by step, explaining your reasoning."
        jsonl_content = client.download_dataset_jsonl(
            project_id,
            task_id,
            dataset_id,
            split_name,
            format_type,
            data_strategy,
            custom_system_message,
            custom_thinking_instructions
        )
        
        # 保存到文件
        output_file = "test_dataset.jsonl"
        with open(output_file, "wb") as f:
            f.write(jsonl_content)
        
        print(f"数据集已下载到 {output_file}")
    except Exception as e:
        print(f"下载数据集失败: {str(e)}")

if __name__ == "__main__":
    main()

