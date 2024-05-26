import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

# Введите ваше решение ниже


def check_multiplicity(amount):
    if amount % MULTIPLICITY != count:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        

def deposit(amount):
    global bank_account, operations
    check_multiplicity(amount)
    if amount % MULTIPLICITY == count:
        commission = amount * PERCENT_DEPOSIT
        bank_account += amount
        operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")


def withdraw(amount):
    global bank_account, operations
    check_multiplicity(amount)
    commission = calculate_commission(amount)
    if amount + commission > bank_account:
        operations.append(f"Недостаточно средств. Сумма с комиссией {int(amount + commission)} у.е. На карте "
                          f"{bank_account} у.е.")
    else:
        bank_account -= amount + commission
        operations.append(f"Снятие с карты {amount} у.е. Процент за снятие {commission} у.е.. Итого "
                          f"{bank_account} у.е.")


def calculate_commission(amount):
    commission = amount * PERCENT_REMOVAL
    if commission < MIN_REMOVAL:
        commission = MIN_REMOVAL
    elif commission > MAX_REMOVAL:
        commission = MAX_REMOVAL
    return commission


def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        bank_account -= tax
        operations.append(f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е.")
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")


deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()
print(operations)
