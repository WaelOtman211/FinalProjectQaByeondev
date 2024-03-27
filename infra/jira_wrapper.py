import os
from dotenv import load_dotenv
from jira import JIRA

from infra.config_handler import ConfigHandler


class JiraClient:
    def __init__(self):
        load_dotenv()
        config_file_path = r'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\infra\config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.jira_url = self.config_handler.get_config_value('jira_url')
        self.TOKEN = os.getenv("JIRA_TOKEN")
        self.auth_jira = JIRA(basic_auth=('waelotman211@gmail.com', self.TOKEN), options={'server': self.jira_url})

    def create_issue(self, summary, description, project_key, issue_type='Bug'):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
        new_issue = self.browser.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key
