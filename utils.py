def inRange(number: float, minValue: float, maxValue: float) -> float:
    return max(min(number, maxValue), minValue)
