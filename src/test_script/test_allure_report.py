import allure
import pytest
import random


@pytest.fixture(autouse=True)
@allure.step('Print welcome string')
def welcome_string():
    print('Welcome everyone!')


@allure.step('Create a random odd number')
def create_odd_number():
    a = random.randint(0, 100)

    while a % 2 == 0:
        a = random.randint(0, 10)

    return a


@allure.step('Verify the result of {x} + {y}')
def verify(x, y):
    assert (x + y) % 2 == 0, 'Failed.'


@allure.suite('Sum operator')
@allure.title('Test case: Sum of 2 odd numbers')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Math Operator')
@allure.description_html("""
<h4>Test case: Sum of 2 odd numbers<h4>
<ol>
    <li>Generate odd number 'x'</li>
    <li>Generate odd number 'y'</li>
    <li>Compute z = 'x + y'</li>
    <li>Verify z is even</li>
</ol>
""")
def test_sum_of_two_odd_number():
    with allure.step('Generate 2 random odd numbers'):
        x = create_odd_number()
        y = create_odd_number()

    with allure.step('Verify the sum of 2 generated number is even number'):
        verify(x, y)

#
