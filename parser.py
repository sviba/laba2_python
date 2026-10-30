import re

class DataValidator:
    def __init__(self) -> None:
        self.pattern = re.compile(
            r"\b(?:0[1-9]|[12][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.(?:[12][0-9]{3})\b"
        )
    
    def validate_text(self,text: str) -> list[str]:
        return self.pattern.findall(text)
    
    def validate_file(self,file: str) -> list[str]:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return self.validate_text(f.read())
        except FileNotFoundError:
            print(f"Ошибка: файл '{file}' не найден.")
            return []
        except OSError as exc:
            print(f"Ошибка чтения файла: {exc}")
            return []