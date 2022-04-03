# Import pathlib
from pathlib import Path

# Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

 # Test_Save_CSV Function
def test_save_csv():
    qualifying_loans = "test"
    csvpath = Path("./tests/qualifying_loans.csv")

    fileio.save_csv(
        csvpath,
        qualifying_loans,
        [
            # Headers for outputted csv file
            "lender",
            "max_loan_amount",
            "max_loan_to_value",
            "max_debt_to_income",
            "min_credit_score",
            "interest_rate",
        ],
    )

    assert csvpath.exists()


def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375


def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84


