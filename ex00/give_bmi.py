def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Compute BMI values from height and weight lists."""
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must have the same size")
        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("Height must contain only numbers")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("Weight must contain only numbers")
        if any(h <= 0 for h in height):
            raise ValueError("Height must be positive")
        if any(w <= 0 for w in weight):
            raise ValueError("Weight must be positive")
        return [w / (h ** 2) for h, w in zip(height, weight)]
    except (ValueError, TypeError) as error:
        print(f"An error occurred: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list indicating which BMI values exceed the limit."""
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("BMI list must contain only numbers")
        return [value > limit for value in bmi]
    except (ValueError, TypeError) as error:
        print(f"An error occurred: {error}")
        return []


def main():
    """Run basic checks for BMI utilities with error handling."""


if __name__ == "__main__":
    main()
