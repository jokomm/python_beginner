"""Tests for Bank."""

from bank import Person, Bank


person1 = Person("Mart", "Juur", 55)
person2 = Person("Margus", "Juur", 23)
person3 = Person("Liis", "Liiv", 44)
bank1 = Bank("TalBank")
bank2 = Bank("Bank2")
a1 = person1.bank_account
a2 = person2.bank_account
a3 = person3.bank_account


def test_person():
    """Testing Person."""
    assert person1.first_name == "Mart"
    assert person2.last_name == "Juur"
    assert person3.age == 44
    assert person1.full_name == "Mart Juur"


def test_bank_add_customer():
    """Testing Person."""
    pass


def test_bank_remove_customer():
    """Testing Person."""
    pass


def test_deposit():
    """Testing Person."""
    assert a1.deposit(100) == 100
    assert a2.deposit(100) == 100


def test_withdraw():
    """Testing Person."""
    assert a1.withdraw(10) == 90
    assert a2.withdraw(50) == 50


def test_transfer():
    """Testing Person."""
    pass


def test_account_statement():
    """Testing Person."""
    pass


def test_debit_turnover():
    """Testing Person."""
    pass


def test_account_number():
    """Testing Person."""
    assert len(a1.number) == 20
