
注意：Markdown中代码块较多。若粘贴后格式有问题，不影响今天验收，内容完整即可。

---

# 十、第9步：编写README.md

打开`README.md`，填写：

```markdown
# 机电设备台账检查器

## 项目目的

本项目用于训练Python工程开发能力，并逐步实现机电设备台账的自动检查。

## 当前版本

V0.0

## 当前功能

- 检查Python运行环境；
- 输出操作系统信息；
- 检查项目必要目录是否存在。

## 项目结构

- `docs/`：项目文档；
- `sample_data/`：测试数据；
- `outputs/`：程序输出；
- `env_check.py`：环境检查程序；
- `environment.md`：开发环境记录。

## 运行方法

在项目根目录打开PowerShell，执行：

```powershell
python .\env_check.py
