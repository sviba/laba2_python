from parser import DataValidator

def main() -> None:
    validator = DataValidator()
    # ... 
    sample_text = (
        "25.10.2024"
        "32.10.2025"
        "14.14.2020"
        "31.10.2027"
    )
    found_dates = validator.validate_text(sample_text)
    # ...

if __name__ == "__main__":
    main()