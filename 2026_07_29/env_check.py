
"""检查当前Python开发环境和项目目录。"""

from datetime import datetime
from pathlib import Path
import platform
import sys


def main() -> None:
    """输出Python、操作系统和项目目录信息。"""

    project_dir = Path(__file__).resolve().parent
    required_directories = ["docs", "sample_data", "outputs"]

    print("=" * 50)
    print("开发环境检查")
    print("=" * 50)
    print(f"检查时间：{datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Python版本：{sys.version.split()[0]}")
    print(f"Python路径：{sys.executable}")
    print(f"操作系统：{platform.system()} {platform.release()}")
    print(f"项目目录：{project_dir}")
    print("-" * 50)

    for directory_name in required_directories:
        directory_path = project_dir / directory_name

        if directory_path.is_dir():
            status = "正常"
        else:
            status = "缺失"

        print(f"{directory_name:<15}：{status}")

    print("=" * 50)
    print("环境检查结束")


if __name__ == "__main__":
    main()
