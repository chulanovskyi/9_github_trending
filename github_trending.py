import datetime
import requests


REPOS_TO_GET = 20
DAYS_BEFORE = 7


def get_trending_repositories(top_size, from_date):
    api_params = {'q': 'created:>=%s' % from_date, 'sort': 'stars'}
    repos = requests.get(
        'https://api.github.com/search/repositories',
        params=api_params).json()
    return repos['items'][:top_size]
    

def get_start_date():
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=DAYS_BEFORE)
    return start_date


def pprint_repo(repo):
    print('Stars: {stars} | Issues: {issues}\n{repo_link}\n'.format(
        stars=repo['stargazers_count'],
        issues=repo['open_issues'],
        repo_link=repo['html_url']))


if __name__ == '__main__':
    repos = get_trending_repositories(REPOS_TO_GET, get_start_date())
    for repo in repos:
        pprint_repo(repo)
