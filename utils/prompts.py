from ast import main
from os import read
from tarfile import data_filter

from utils.logger_handler import logger
from utils.path_tool import get_abs_path

from utils.config_handler import prompts_config



def load_system_prompts():
    try:
        system_prompts_path  = get_abs_path(prompts_config["main_prompts_path"])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yml中没有main_prompts_path配置项")
        raise e

    print(system_prompts_path)
    try:
        return open(system_prompts_path,"r",encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_system_prompts]解析系统提示词错误")
        raise e
    
def load_rag_prompts():
    try:
        rag_prompts_path  = get_abs_path(prompts_config["rag_summarize_prompts_path"])
    except KeyError as e:
        logger.error(f"[load_rag_prompt]在yml中没有rag_summarize_prompts_path配置项")
        raise e

    try:
        return open(rag_prompts_path,"r",encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[rag_summarize_prompts_path]解析rag总结错误")
        raise e
    
def load_report_prompts():
    try:
        report_prompts_path  = get_abs_path(prompts_config["report_prompts_path"])
    except KeyError as e:
        logger.error(f"[load_rag_prompt]在yml中没有report_prompts_path配置项")
        raise e

    try:
        return open(report_prompts_path,"r",encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[report_prompts_path]解析rag总结错误")
        raise e

        