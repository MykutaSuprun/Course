balance=1000
def transaction(amount,_type):
    def deposit(amount):
        global balance
        balance += amount
        return(balance)
    def withdrawal(amount):
        global balance
        balance -= amount
        return(balance)
    if _type=='deposit':
        deposit(amount)
    elif _type=='withdrawal':
        withdrawal(amount)
    return(balance)

print(transaction(200, "deposit"))
