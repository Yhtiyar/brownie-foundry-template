from brownie import Counter, accounts
from brownie.test import given, strategy
from hypothesis import settings
import pytest


@pytest.fixture(scope="module", autouse=True)
def counter():
    contract = Counter.deploy({"from": accounts[0]})
    contract.setNumber(0, {"from": accounts[0]})
    return contract


def test_increment(counter, accounts):
    counter.increment({"from": accounts[0]})
    assert counter.number() == 1


@given(number=strategy("uint", max_value=100))
@settings(max_examples=10)
def test_setNumber(counter, accounts, number):
    counter.setNumber(number, {"from": accounts[0]})
    assert counter.number() == number
