from dataset.dataset_api import HetuAIDataGenClient
import json
import os

def main():
    # 初始化客户端
    client = HetuAIDataGenClient(base_url="http://localhost:8000")
    
    # 测试参数
    project_id = "250615285993"
    task_id = "316831576302"
    
    # 测试生成分类
    print("测试生成分类...")
    try:
        categories_input = {
            "node_path": ["root"],
            "num_subtopics": 5,
            "model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "provider": "together_ai",
            "human_guidance": "生成与人工智能相关的分类",
            "drop_unsupported_params": True 
        }
        
        categories_result = client.generate_categories(project_id, task_id, categories_input)
        print(f"生成的分类: {json.dumps(categories_result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"生成分类失败: {str(e)}")

    # 测试生成样本
    print("\n测试生成样本...")
    try:
        samples_input = {
            "topic": ["人工智能应用"],
            "num_samples": 3,
            "model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
            "provider": "together_ai",
            "human_guidance": "生成关于人工智能在医疗领域应用的样本"
        }
        
        samples_result = client.generate_samples(project_id, task_id, samples_input)
        print(f"生成的样本: {json.dumps(samples_result, indent=2, ensure_ascii=False)}")
        
        # 保存第一个生成的样本（如果有）
        if hasattr(samples_result, 'samples') and len(samples_result.samples) > 0:
            first_sample = samples_result.samples[0]
            
            # 测试保存单个样本
            print("\n测试保存样本...")
            sample_data = {
                "input": first_sample.input,
                "topic_path": "人工智能/医疗应用",
                "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "input_provider": "together_ai",
                "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "output_provider": "together_ai",
                "prompt_method": "default",
                "human_guidance": "医疗领域的人工智能应用"
            }
            
            save_result = client.save_sample(project_id, task_id, sample_data)
            print(f"保存的样本: {json.dumps(save_result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"生成或保存样本失败: {str(e)}")

    print("\n测试批量保存样本...")
    try:
        batch_data = {
            "samples": [
                {
                    "input": "人工智能在医疗诊断中的应用有哪些？",
                    "topic_path": ["人工智能", "医疗应用", "诊断"],
                    "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "input_provider": "together_ai",
                    "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "output_provider": "together_ai",
                    "prompt_method": "simple_prompt_builder",  # 使用有效的 PromptId
                    "human_guidance": "医疗诊断中的人工智能应用"
                },
                {
                    "input": "人工智能在药物研发中的应用有哪些？",
                    "topic_path": ["人工智能", "医疗应用", "药物研发"],
                    "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "input_provider": "together_ai",
                    "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                    "output_provider": "together_ai",
                    "prompt_method": "simple_prompt_builder",  # 使用有效的 PromptId
                    "human_guidance": "药物研发中的人工智能应用"
                }
            ]
        }

        
        batch_result = client.save_samples_batch(project_id, task_id, batch_data)
        print(f"批量保存结果: {json.dumps(batch_result, indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"批量保存样本失败: {str(e)}")


    # 测试从文件导入样本
    # print("\n测试从文件导入样本...")
    # try:
    #     # 使用已存在的CSV文件
    #     temp_file = os.path.abspath("dataset/temp_samples.csv")
        
    #     # 确保文件存在
    #     if not os.path.exists(temp_file):
    #         print(f"错误: 文件 {temp_file} 不存在")
    #         # 可以选择在这里创建文件或退出
        
    #     # 导入文件
    #     request_data = {
    #         "prompt_method": "simple_prompt_builder",
    #         "input_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
    #         "output_model_name": "Qwen/Qwen2.5-72B-Instruct-Turbo",
    #         "output_provider": "together_ai",
    #         "input_provider": "together_ai",
    #     }
        
    #     import_result = client.import_samples_from_file(
    #         project_id, 
    #         task_id, 
    #         temp_file,
    #         request_data
    #     )
    #     print(f"文件导入结果: {json.dumps(import_result, indent=2, ensure_ascii=False)}")
        
    #     # 不要删除文件，因为它是预先存在的资源
    # except Exception as e:
    #     print(f"从文件导入样本失败: {str(e)}")
    
    print("\n所有测试完成!")



if __name__ == "__main__":
    main()
