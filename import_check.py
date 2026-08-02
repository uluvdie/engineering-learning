"""验证当前Python解释器及openpyxl安装位置。"""

from pathlib import Path
import sys

import openpyxl


def main() -> None:
    """输出解释器、虚拟环境和openpyxl信息。"""

    is_virtual_environment = sys.prefix != sys.base_prefix

    print("=" * 60)
    print("Python依赖环境检查")
    print("=" * 60)
    print(f"当前解释器：{sys.executable}")
    print(f"Python版本：{sys.version.split()[0]}")
    print(f"虚拟环境：{'是' if is_virtual_environment else '否'}")
    print(f"当前环境目录：{sys.prefix}")
    print(f"基础Python目录：{sys.base_prefix}")
    print(f"openpyxl版本：{openpyxl.__version__}")
    print(f"openpyxl位置：{Path(openpyxl.__file__).resolve()}")
    print("=" * 60)
    print("openpyxl导入成功")


if __name__ == "__main__":
    main()