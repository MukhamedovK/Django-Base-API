from .models import User


def registration_check(formData):
    username = formData.get("username")
    email = formData.get("email")
    password1 = formData.get("password")
    password2 = formData.get("repeat_password")

    if len(password2) < 8:
        return "Password must be at least 8 characters"
    if password1 != password2:
        return "Passwords don't match"
    if User.objects.filter(email=email).exists():
        return "Email already taken"
    if username.isdigit():
        return "Username mustn't contain only numbers"
    if User.objects.filter(username=username).exists():
        return "Username already taken"

    return None