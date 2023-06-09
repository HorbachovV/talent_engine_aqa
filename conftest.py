import pytest
from src.user import User
from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config


@pytest.fixture(scope='session') # session|package|module|function
def user_fixture():
    # create a user -> precondition
    user_name = User.username
    user = dict(name=user_name)
    print(f"User '{user_name}' created")

    # execute test -> test step
    yield user

    # remove a user -> postconditions
    user = None
    print(f"User '{user_name}' removed")

def pytest_html_report_title(report):
    report.title = "TE Apr 2023!"

@pytest.fixture(scope="session")
def fixture_git_hub_api_client():
    api = GitHubAPIClient()
    api .login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api
    
    api.logout()

@pytest.fixture(scope='module')
def fixture_git_hub_api_client_search_repo():
    api = GitHubAPIClient()
    api.login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api.search_repo

    api.logout()

# @pytest.fixture
# def data_provider():
#     def _(type_of_data):
#         API_DATA.get_date(type_of_data)

#     yield _