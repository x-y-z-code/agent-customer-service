"""
为整个工程提供统一的绝对路径
"""

import os



def get_project_root() -> str:
    """
    获取项目的根目录
    """
    
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    return  os.path.dirname(current_dir)

def get_abs_path(relative_path: str) -> str:
    """
    获取项目绝对路径
    """
    project_root = get_project_root()
    return os.path.join(project_root,relative_path)