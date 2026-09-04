def validate_description(desc: str) -> bool:
    if len(desc) > 30:
        return False

    return True

def validate_categories(category: list[str]) -> bool:
    for i in category:
        if type(i) != str:
            return False

    if not any(category):
        return False

    return True

def validate_cost(cost: float) -> bool:
    if cost < 0:
        return False

    return True