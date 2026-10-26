import re

class DataValidator:
    def __init__() -> None:
        self.pattern = re.compile(
            r"\b(?:0[1-9]|[12][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.(?:[12][0-9]{3})\b"
        )
    
    def validate_text(self,text: str) -> list[str]:
        # ...
    
    def validate_file(self,file: str) -> list[str]:
        # ...