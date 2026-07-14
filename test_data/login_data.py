# 正确登录数据
VALID_LOGIN = {
    "username": "standard_user",
    "password": "secret_sauce",
}

# 错误登录数据：(用户名, 密码, 期望错误信息)
INVALID_LOGIN_DATA = [
    (
        "standard_user",
        "wrong_password",
        "Username and password do not match"
    ),
    (
        "locked_out_user",
        "secret_sauce",
        "Sorry, this user has been locked out"
    ),
    (
        "",
        "secret_sauce",
        "Username is required"
    ),
    (
        "standard_user",
        "",
        "Password is required"
    ),
]