from parser import DataValidator

def main() -> None:
    validator = DataValidator()
    sample_text = (
        "25.10.2024 "
        "32.10.2025 "
        "14.14.2020 "
        "31.10.2027"
    )
    print(f"Исходный текст: {sample_text}\n")
    found_dates = validator.validate_text(sample_text)
    print(f"Найденные даты: {found_dates}")

if __name__ == "__main__":
    main()