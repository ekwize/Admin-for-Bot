def start_message(first_name: str, user_exists: bool):
    if user_exists:
        return(
            f"""
                <b>We've already met, {first_name}!</b>
            """
        )
    
    return (
        f"""
            <b>Hello, {first_name}!</b>
        """
    )