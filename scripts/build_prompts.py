from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
body = (root / "references" / "original-sanitized.md").read_text(encoding="utf-8")
# 去掉文档存档说明，保留完整正文、所有细则与例子。
body = re.sub(r"^> [^\n]*\n+", "", body, count=1).strip()
agent = """先读取我指定的论文材料及项目约定，定位正文、参考文献和结果来源。只修改本次指定范围；检查已有修改，保留无关内容。具备工具时实际核验，缺少工具或材料时说明未完成的检查。正式交付完整英文替换内容及对应中文，简述修改和验证结果。不要仅返回差异片段。
"""
web = """你是我的学术写作助手。以下是本次对话的写作规范。只根据我粘贴、上传或你实际能够读取的材料工作，不假定能访问我的本地文件。材料不足时只问影响当前任务的关键问题。能直接完成的部分先完成。没有检索或编译能力时如实说明，不声称已核验文献或版面。不要要求安装技能。正式输出完整英文替换内容与对应中文。
"""
for name, intro in [("codex.md", "面向 Codex 的任务提示词。\n\n" + agent), ("claude-code.md", "面向 Claude Code 的任务提示词。\n\n" + agent), ("chat-web.md", web)]:
    result = intro + "\n" + body + "\n\n## 本次任务\n\n任务：请填写修改目标。\n材料：请附上正文或指定可访问文件。\n范围及约束：请填写需要保留的内容、字数或格式要求；未填写时按上述规范执行。\n"
    (root / "prompts" / name).write_text(result, encoding="utf-8")
print("Built 3 standalone prompts with the complete detailed writing specification.")
