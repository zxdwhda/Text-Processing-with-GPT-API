# config.py

# 项目的配置设置

# GPT 服务的 API 网址
API_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

# 相关密钥
CONFIG = {
    'api_url': 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    'api_key': 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'prompt_word': '''# 角色
你是一个精准的信息处理器，能够将上传的各类信息转化为段落形式的文章。在处理过程中，严格遵循不添加、不删除文字的原则，合理运用标点符号，使输出内容清晰易读，符合纯文本的格式要求。

## 技能
### 技能 1: 信息处理
1. 当接收到上传的信息后，仔细分析其内容结构。
2. 按照句子和语义的逻辑，合理添加标点符号，将信息分割成段落。

## 限制:
- 严禁对上传的信息进行任何添加或删除操作。
- 输出的文章必须是纯文本格式，不得包含任何特殊格式或代码。
- 严格按照信息的原有内容和逻辑进行标点添加和段落划分。'''
}

# 默认切片大小，用于拆分输入文件
SLICE_SIZE = 300  # 根据您的需要调整此值

# 相关函数值
if __name__ == "__main__":
    print(f"API URL: {API_URL}")
    print(f"Prompt Word: {PROMPT_WORD}")
    print(f"Slice Size: {SLICE_SIZE}")