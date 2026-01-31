
import pytest
from typer.testing import CliRunner
from saki.cli import app
from unittest.mock import MagicMock, patch

runner = CliRunner()

@pytest.fixture
def mock_config_manager():
    with patch("saki.commands.repo.config_manager") as mock:
        mock.get_repositories.return_value = [{"name": "mock-repo", "url": "http://mock", "type": "git"}]
        yield mock

def test_repo_list(mock_config_manager):
    result = runner.invoke(app, ["repo", "list"])
    assert result.exit_code == 0
    assert "mock-repo" in result.stdout

def test_repo_add(mock_config_manager):
    result = runner.invoke(app, ["repo", "add", "new-repo", "http://new"])
    assert result.exit_code == 0
    mock_config_manager.add_repository.assert_called_with("new-repo", "http://new", "git")
    assert "added successfully" in result.stdout

def test_repo_remove(mock_config_manager):
    result = runner.invoke(app, ["repo", "remove", "old-repo"])
    assert result.exit_code == 0
    mock_config_manager.remove_repository.assert_called_with("old-repo")
    assert "removed" in result.stdout
