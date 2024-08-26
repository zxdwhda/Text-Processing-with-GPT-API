import os
import json
import requests
from config import CONFIG

def build_request(slice_content, prompt_word):
    """
    Builds the request payload for the GPT API.

    Args:
        slice_content (str): The content of the slice to be processed.
        prompt_word (str): The prompt word to attach to the request.

    Returns:
        dict: The request payload.
    """
    # 生成请求有效载荷
    request_payload = {
        "model": "qwen-turbo",  # 使用适当的模型 ID
        "prompt": f"{prompt_word} {slice_content}",# 提示词 切片内容
        "max_tokens": 1024,  # 根据需要调整最大令牌数
        "temperature": 0.5,  # 根据需要调节温度，术语名称，影响生成文本随机性的参数。
        # 数值越小，输出越确定。
        # 一般不需要动
    }
    return request_payload


def call_gpt_api(api_url, request_payload, api_key):
    """
    Sends a request to the GPT API and receives the response.

    Args:
        api_url (str): The URL of the GPT API.
        request_payload (dict): The request payload.
        api_key (str): The API key for authentication.

    Returns:
        dict: The API response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # 发送 POST 请求
    response = requests.post(api_url, headers=headers, json=request_payload)

    # 检查响应状态码
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get a response from the GPT API: {response.text}")


def process_slices_with_gpt(input_directory, api_url, prompt_word, output_directory):
    """
    Processes each slice using the GPT API with a specific cue word attached.

    Args:
        input_directory (str): Directory containing the input slices.
        api_url (str): The URL of the GPT API.
        prompt_word (str): The prompt word to attach to the request.
        output_directory (str): Directory to save the processed slices.
    """
    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over each slice file
    for slice_file_name in os.listdir(input_directory):
        if slice_file_name.endswith('.txt'):
            # 遍历每个切片文件
            slice_file_path = os.path.join(input_directory, slice_file_name)
            with open(slice_file_path, 'r', encoding='utf-8') as slice_file:
                slice_content = slice_file.read()

            # 生成请求有效载荷
            request_payload = build_request(slice_content, prompt_word)

            # 调用 GPT 应用程序接口
            try:
                api_response = call_gpt_api(api_url, request_payload, CONFIG['api_key'])
                # 从响应中提取生成的文本
                generated_text = api_response['choices'][0]['text'].strip()
            except Exception as e:
                print(f"Error processing file {slice_file_name}: {e}")
                continue

            # 将处理后的切片写入新文件
            output_file_path = os.path.join(output_directory, slice_file_name)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(generated_text)


if __name__ == "__main__":
    # Example usage:
    input_directory = 'sliced_files'
    api_url = CONFIG['api_url']
    prompt_word = CONFIG['prompt_word']
    output_directory = 'processed_files'
    process_slices_with_gpt(input_directory, api_url, prompt_word, output_directory)