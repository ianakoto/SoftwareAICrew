import os
from dotenv import load_dotenv, find_dotenv
from langtrace_python_sdk import langtrace


def load_env():
    _ = load_dotenv(find_dotenv())


def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def get_serper_api_key():
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key


def init_langtrace_api_key():
    load_env()
    langtrace_api_key = os.getenv("LANGTRACE_API_KEY")
    langtrace.init(api_key=langtrace_api_key)


def get_lantrace_url():
    load_env()
    langtrace_url = os.getenv("LANGTRACE_URL")
    return langtrace_url
