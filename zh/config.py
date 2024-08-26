# config.py

# 项目的配置设置

# GPT 服务的 API 网址
API_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

# 附加到每个 API 请求的提示词
PROMPT_WORD = '''把上传的txt文件输出成文章的形式（段落形式），并以代码块的形式发给我，不要添加、删除任何文字，可以适当添加标点符号。
以下是根据提供一部分示例内容以便你能够展示如何操作


```markdown
Hi 大家好
我觉得说我是计算机系杰出校友
有点不敢当
我就是很多年没有回来
这次回国
很多年没回来
想见一见本科导师俞勇老师
和我的实验室
我的整个 A I 的启蒙导师吕宝粮老师
```

```markdown
Hi！大家好，我觉得说我是计算机系杰出校友，有点不敢当，我就是很多年没有回来，这次回国，很多年没回来，想见一见本科导师俞勇老师，和我的实验室，我的整个 AI 的启蒙导师吕宝粮老师。
```'''

# 默认切片大小，用于拆分输入文件
SLICE_SIZE = 300  # 根据您的需要调整此值

# 相关函数值
if __name__ == "__main__":
    print(f"API URL: {API_URL}")
    print(f"Prompt Word: {PROMPT_WORD}")
    print(f"Slice Size: {SLICE_SIZE}")