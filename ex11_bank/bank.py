"""Bank."""
import datetime
import random


class PersonError(Exception):
    """Person error."""

    pass


class TransactionError(Exception):
    """Transaction error."""

    pass


class Person:
    """Person class."""

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Person constructor.

        :param first_name: first name
        :param last_name: last name
        :param age: age, must be greater than 0
        """
        if age <= 0:
            raise PersonError()
        self._age = age
        if not last_name:
            raise PersonError()
        self.last_name = last_name
        if not first_name:
            raise PersonError()
        self.first_name = first_name
        self.bank_account = None

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Set person's age. Must be greater than 0."""
        if value <= 0:
            raise PersonError()
        else:
            self._age = value

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


class Bank:
    """Bank class."""

    def __init__(self, name: str):
        """
        Bank constructor.

        :param name: name of the bank
        """
        self.name = name
        self.customers = []
        self.transactions = []

    def add_customer(self, person: Person) -> bool:
        """
        Add customer to bank.

        :param person: person object
        :return: was customer successfully added
        """
        if person not in self.customers:
            person.bank_account = Account(0, person, self)
            self.customers.append(person)
            return True
        return False

    def remove_customer(self, person: Person) -> bool:
        """
        Remove customer from bank.

        :param person: person object
        :return: was customer successfully removed
        """
        if person in self.customers:
            self.customers.remove(person)
            person.bank_account = None
            return True
        return False

    def __repr__(self) -> str:
        """
        Bank representation.

        :return: name of the bank
        """
        return self.name


class Transaction:
    """Transaction class."""

    def __init__(self, amount: float, date: datetime.date, sender_account: 'Account', receiver_account: 'Account',
                 is_from_atm: bool):
        """
        Transaction constructor.

        :param amount: value
        :param date: date of the transaction
        :param sender_account: sender's object
        :param receiver_account: receiver's object
        :param is_from_atm: is transaction from atm
        """
        self.amount = amount
        self.date = date
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.is_from_atm = is_from_atm

    def __repr__(self) -> str:
        """
        Transaction representation.

        :rtype: object's values displayed in a nice format
        """
        if self.is_from_atm:
            return f"({self.amount} €) ATM"
        return f"({self.amount} €) {self.sender_account.person.full_name} -> {self.receiver_account.person.full_name}"


class Account:
    """Account class."""

    def __init__(self, balance: float, person: Person, bank: 'Bank'):
        """
        Account constructor.

        :param balance: initial account balance
        :param person: person object
        :param bank: bank object
        """
        self._balance = balance
        self.person = person
        self.bank = bank
        self.transactions = []
        self.number = "EE" + "".join([str(random.randint(0, 9)) for _ in range(18)])

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return self._balance

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        if amount <= 0:
            raise TransactionError()
        self._balance = self.balance + amount
        if is_from_atm:
            transaction = Transaction(amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(transaction)
            self.bank.transactions.append(transaction)

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        if amount <= 0 or self._balance - amount < 0:
            raise TransactionError()
        self._balance -= amount
        if is_from_atm:
            trans = Transaction(-amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(trans)
            self.bank.transactions.append(trans)

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""
        fee = 5
        if receiver_account.bank == self.bank:  # if receiver in different bank, take fee 5 eur
            fee = 0
        if self.balance < amount + fee or self == receiver_account:  # if not enough money for fee or receiver=sender
            raise TransactionError()
        self.withdraw(amount, False)
        receiver_account.deposit(amount, False)
        trans = Transaction(amount, datetime.date.today(), self, receiver_account, False)
        self.transactions.append(trans)
        self.bank.transactions.append(trans)
        if self.bank == receiver_account.bank:
            receiver_account.transactions.append(trans)
        else:
            receiver_account.bank.transactions.append(trans)

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        result = list(filter(lambda x: from_date <= x.date <= to_date, self.transactions))
        return result

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total income in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: debit turnover number
        """
        turnover = 0
        for transaction in self.transactions:
            if from_date <= transaction.date <= to_date:
                if transaction.receiver_account == self:
                    turnover += transaction.amount
        return turnover

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total expenditure in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: credit turnover number
        """
        turnover = 0
        for transaction in self.transactions:
            if from_date <= transaction.date <= to_date:
                if transaction.receiver_account == self:
                    turnover -= transaction.amount
        return turnover

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get net turnover (income - costs) in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: net turnover number
        """
        return self.get_debit_turnover(from_date, to_date) + self.get_credit_turnover(from_date, to_date)

    def __repr__(self) -> str:
        """
        Account representation.

        :return: account number
        """
        return self.number

    if __name__ == '__main__':
        person = Person("Mart", "Juur", 55)
        person2 = Person("Margus", "Juur", 23)
        bank = Bank("TalBank")
        bank.add_customer(person)
        bank.add_customer(person2)
        print(person.bank_account)

        a1 = person.bank_account
        a2 = person2.bank_account
        d = datetime.date.today()

        a1.deposit(100)
        a2.deposit(100)
        print(a1.get_debit_turnover(d, d))
        print(a2.get_debit_turnover(d, d))
        print(a1.get_credit_turnover(d, d))
        print(a2.get_credit_turnover(d, d))
        a1.withdraw(10)
        a2.withdrraw(50)
        print(a1.get_debit_turnover(d, d))
        print(a2.get_debit_turnover(d, d))
        print(a1.get_credit_turnover(d, d))
        print(a2.get_credit_turnover(d, d))
        try:
            a1.transfer(200, a2)
            print("Fail")
        except TransactionError:
            print("Ok")

        a1.transfer(10, a2)
        print(a1.get_debit_turnover(d, d))
        print(a2.get_debit_turnover(d, d))
        print(a1.get_credit_turnover(d, d))
        print(a2.get_credit_turnover(d, d))

        bank2 = Bank("Bank2")
        person3 = Person("Liis", "Liiv", 44)
        bank2.add_customer(person3)
        a3 = person3.bank_account

        a1.transfer(10, a3)
