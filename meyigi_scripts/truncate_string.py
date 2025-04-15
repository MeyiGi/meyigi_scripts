
def truncate_string(s: str, max_length: int, triple_dot: bool = True) -> str:
    """Truncates a string if it exceeds a given max length."""
    if triple_dot:
        return s[:max_length] + "..." if len(s) > max_length else s
    return s[:max_length] if len(s) > max_length else s