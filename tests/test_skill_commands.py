
import pytest
from typer.testing import CliRunner
from saki.cli import app
from saki.core.install import SkillInjector
from pathlib import Path
from unittest.mock import MagicMock, patch

runner = CliRunner()

@pytest.fixture
def mock_injector():
    with patch("saki.commands.skill.injector") as mock:
        yield mock

@pytest.fixture
def mock_config():
    with patch("saki.commands.skill.config_manager") as mock:
        # returns dummy cursor config
        mock.get_tool_config.return_value = {"global": ".cursor/rules"}
        yield mock

def test_inject_skill_command_calls_injector(mock_injector, mock_config):
    # Mock input confirm
    result = runner.invoke(app, ["skill", "inject", "saki", "--target", "cursor", "--global", "--force"])
    
    assert result.exit_code == 0
    mock_injector.inject.assert_called_once()
    assert "saki" in str(mock_injector.inject.call_args[0][0]) # Check source path contains saki

def test_inject_unknown_target(mock_config):
    mock_config.get_tool_config.return_value = None # simulate unknown tool
    result = runner.invoke(app, ["skill", "inject", "saki", "--target", "unknown_tool"])
    
    assert result.exit_code == 0 # Typer defaults to 0 unless exception raised, but logic should print error
    assert "Unknown target" in result.stdout

def test_inject_alias(mock_injector, mock_config):
    # Test the root level 'inject' command alias
    result = runner.invoke(app, ["inject", "saki", "--target", "cursor", "--global", "--force"])
    assert result.exit_code == 0
    mock_injector.inject.assert_called()

def test_list_skills():
    result = runner.invoke(app, ["skill", "list"])
    assert result.exit_code == 0
    assert "Available Skills" in result.stdout
    assert "saki" in result.stdout
