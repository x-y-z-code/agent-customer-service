from abc import ABC,abstractmethod
from ast import Pass
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import BaseChatModel,ChatTongyi
from utils.config_handler import rag_config
from langchain_community.embeddings import DashScopeEmbeddings


class BaseModelFactory(ABC):
    
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatTongyi(model=rag_config["chat_model_name"],api_key=rag_config["chat_model_api_key"])
    

class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"],dashscope_api_key=rag_config["chat_model_api_key"])
    
chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()