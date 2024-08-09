# prompts/core.py

from string import Template
from abc import ABC, abstractmethod
import json

__all__ = [
    "AbstractPromptTemplate",
    "BasePromptTemplate", 
    "BaseConversationTemplate", 
]


class AbstractPromptTemplate(ABC):
    @abstractmethod
    def format(self, **kwds) -> str:
        raise NotImplementedError
    
    def __call__(self, **kwds) -> str:
        return self.format(**kwds)


class BasePromptTemplate(Template, AbstractPromptTemplate):
    """Basic Prompt Template Definition with $-delimited substitutions."""

    def __init__(self, template: str):
        Template.__init__(self, template)

    def format(self, **kwds) -> str:
        return self.safe_substitute(**kwds)


class BaseConversationTemplate(Template, AbstractPromptTemplate):
    """Basic Conversational Template Definition."""
    
    def __init__(self, 
                 messages: list):
        self.messages = messages
        Template.__init__(self, 
                          json.dumps(self.messages))

    def format(self, **kwds) -> list:
        return [
            {
                "role": Template(message["role"]).safe_substitute(**kwds),
                "content": Template(message["content"]).safe_substitute(**kwds)
            }
            for message in self.messages
        ]
