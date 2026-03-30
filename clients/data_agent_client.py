import os
import requests
import google.auth
import google.auth.transport.requests


class DataAgentClient:

    BASE_URL = "https://geminidataanalytics.googleapis.com"
    API_VERSION = "v1beta"

    def __init__(
        self,
        project_id=None,
        location=None,
        data_agent_id=None,
        timeout=30,
    ):
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID")
        self.location = location or os.getenv("GCP_LOCATION")
        self.data_agent_id = data_agent_id or os.getenv("DATA_AGENT_ID")
        self.timeout = timeout

        self.session = requests.Session()

    def _get_credentials(self):
        credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        auth_request = google.auth.transport.requests.Request()
        credentials.refresh(auth_request)
        return credentials

    def _get_headers(self):
        credentials = self._get_credentials()

        return {
            "Authorization": f"Bearer {credentials.token}",
            "Content-Type": "application/json"
        }

    def _get_url(self):
        return (
            f"{self.BASE_URL}/{self.API_VERSION}/projects/{self.project_id}"
            f"/locations/{self.location}/dataAgents/{self.data_agent_id}"
        )

    def get_agent(self):

        response = self.session.get(
            self._get_url(),
            headers=self._get_headers(),
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.json()