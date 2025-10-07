def user_level_context(request):
    """Adds user's current English level to every template."""
    if request.user.is_authenticated and hasattr(request.user, "profile"):
        return {"user_english_level": request.user.profile.english_level}
    return {"user_english_level": None}
