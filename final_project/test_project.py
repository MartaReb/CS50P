from project import get_data_from_api
from project import country_list
from project import capital_list
from project import user_answer


def test_user_answer():
    assert user_answer("London","London") == 1
    assert user_answer("Paris","Warsaw") == 0