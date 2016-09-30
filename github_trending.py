import datetime
import requests


REPOS_TO_GET = 20


def get_trending_repositories(top_size, from_date):
    last_week_repos = requests.get(
        'https://api.github.com/search/repositories?q=created:>={a_date}&sort=stars'.format(
            a_date=from_date)).json()
    return last_week_repos['items'][:top_size]
    

def get_last_week():
    today = datetime.date.today()
    week_earlier = today - datetime.timedelta(days=7)
    return week_earlier


def pprint_repo(repo):
    print('Stars: {stars} | Issues: {issues}\n{repo_link}\n'.format(
        stars=repo['stargazers_count'],
        issues=repo['open_issues'],
        repo_link=repo['html_url']))


if __name__ == '__main__':
    repos = get_trending_repositories(REPOS_TO_GET, get_last_week())
    for repo in repos:
        pprint_repo(repo)
