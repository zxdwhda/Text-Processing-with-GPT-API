# Text-Processing-with-GPT-API
This project aims to automate the process of splitting large text files into smaller chunks, processing each chunk through an external GPT API with specific prompts, and then merging the processed chunks back into a single file. It provides a robust solution for efficiently handling large datasets that need to be processed by AI models.

# 项目介绍
该项目旨在自动将大型文本文件分割成小块，通过外部 GPT API 根据特定提示处理每个小块，然后将处理过的小块合并回单个文件。它为高效处理需要由人工智能模型处理的大型数据集提供了一个强大的解决方案。

## 使用场景
1. 对于视频字幕，自动将其拆分成更小的块，直接输出成文章。
2. 对于视频文案，自动将其拆分成更小的块，直接输出成视频字幕。

## 文件结构
项目我们可以将其分为几个主要的模块或文件，每个模块负责不同的任务。

1. **主程序 (`main.py`)**:
   - 这个脚本将作为整个流程的入口点，协调其他模块的功能。
   - 包含主循环或者主函数来执行各个步骤。

2. **文件分片模块 (`file_splitter.py`)**:
   - 负责读取原始文件并按照行数进行分割。
   - 包含用于保存分割后的小文件的函数。

3. **GPT API 调用模块 (`gpt_api_caller.py`)**:
   - 包含与 GPT API 交互的逻辑。
   - 提供函数来构造请求、发送请求以及解析响应。

4. **结果合并模块 (`result_combiner.py`)**:
   - 负责读取所有经过 GPT 处理的文件，并将它们合并成一个单一的文件。
   - 可能需要确保文件按正确的顺序被合并。

5. **配置文件 (`config.py` 或 `settings.py`)**:
   - 存储项目中可能会频繁更改的设置，例如 API 的 URL、提示词、分片大小等。

6. **辅助函数 (`utils.py`)**:
   - 包括一些通用的辅助函数，比如读写文件、日志记录等。

7. **测试文件 (`tests/` 目录)**:
   - 包含单元测试和集成测试脚本，确保各个模块正确工作。

8. **文档 (`README.md`)**:
   - 描述项目的目的、安装指南、如何运行等。

9. **依赖管理 (`requirements.txt` )**:
   - 列出项目所需的 Python 库及其版本。

这里是一个可能的目录结构示例：

```
project/
|-- main.py
|-- file_splitter.py
|-- gpt_api_caller.py
|-- result_combiner.py
|-- config.py
|-- utils.py
|-- tests/
|   |-- test_file_splitter.py
|   |-- test_gpt_api_caller.py
|   |-- test_result_combiner.py
|-- README.md
|-- requirements.txt
```
## LICENSE

<a rel="license" href="https://opensource.org/licenses/MIT"><img alt="MIT License" style="border-width:0" src="https://img.shields.io/badge/license-MIT-blue" /></a><br />
本作品采用<a rel="license" href="https://opensource.org/licenses/MIT">MIT 许可协议</a>进行许可。