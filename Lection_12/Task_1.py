def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print("Customer receipt shown.")


show_customer_receipt(user_type='admin')

try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)
