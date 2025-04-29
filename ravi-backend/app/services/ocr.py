from abc import ABC, abstractmethod

class OCRService(ABC):
    @abstractmethod
    def extract_text(self, image_bytes: bytes) -> str:
        ...