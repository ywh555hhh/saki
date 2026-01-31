import sys
from pathlib import Path
# Fix import path to pick up src/saki package instead of root saki.py
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import pytest
from typer.testing import CliRunner
from saki.cli import app
from saki.core.install import injector
from saki.config import SKILL_SOURCE_DIR
from unittest.mock import MagicMock

runner = CliRunner()

def test_init_command_success(mocker):
    # Mock the inject method on the class to ensure all instances are patched
    mock_inject = mocker.patch('saki.core.install.SkillInjector.inject', return_value=True)
    
    # Run command
    result = runner.invoke(app, ["init", "--target", "test_target"])
    
    print(f"DEBUG Output: {result.stdout}")
    print(f"DEBUG Exit Code: {result.exit_code}")
    if result.exception:
        print(f"DEBUG Exception: {result.exception}")
    
    assert result.exit_code == 0
    assert "Saki is Online" in result.stdout
    
    # Verify call
    mock_inject.assert_called_once()
    args, kwargs = mock_inject.call_args
    # args[0] is source, args[1] is dest
    assert args[0] == SKILL_SOURCE_DIR
    assert args[1].name == "test_target"

def test_init_command_failure(mocker):
    # Mock failure
    mocker.patch.object(injector, 'inject', return_value=False)
    
    result = runner.invoke(app, ["init", "--target", "test_target"])
    
    assert result.exit_code == 1
    
