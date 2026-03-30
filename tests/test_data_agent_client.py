from unittest.mock import patch
from clients.data_agent_client import DataAgentClient


@patch("clients.data_agent_client.DataAgentClient._get_headers")
@patch("clients.data_agent_client.requests.Session.get")
def test_get_agent(mock_get, mock_headers):

    mock_headers.return_value = {"Authorization": "Bearer fake"}

    mock_get.return_value.json.return_value = {
        "name": "agent-test"
    }

    client = DataAgentClient(
        project_id="test",
        location="test",
        data_agent_id="test"
    )

    result = client.get_agent()

    assert result["name"] == "agent-test"