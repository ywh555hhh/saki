
import pytest
from unittest.mock import MagicMock, patch
from saki.cli import interactive_mode
import sys

@pytest.fixture
def mock_questionary():
    with patch("saki.cli.questionary") as mock:
        yield mock

@pytest.fixture
def mock_config_manager():
    with patch("saki.cli.config_manager") as mock:
        # returns dummy config
        mock.get_all_tools.return_value = {
            "cursor": {"name": "Cursor", "global": ".cursor/rules", "local": ".cursor/rules"}
        }
        yield mock

@pytest.fixture
def mock_injector():
    with patch("saki.cli.injector") as mock:
        yield mock

def test_interactive_quit(mock_questionary):
    # Simulate selecting "Quit"
    mock_questionary.select.return_value.ask.return_value = "Quit"
    
    with pytest.raises(SystemExit):
        interactive_mode()

def test_interactive_inject_flow(mock_questionary, mock_config_manager, mock_injector):
    # Sequence of user inputs:
    # 1. Main Action -> Inject Skill
    # 2. Select Tool -> cursor
    # 3. Select Location -> Global
    # 4. Confirm -> Yes
    # 5. Press Enter to Continue
    # 6. Main Action -> Quit (to exit loop)
    
    # We need to set side_effect for each call to select/confirm/etc
    
    # Mock Objects returned by ask()
    mock_questionary.select.side_effect = [
        MagicMock(ask=MagicMock(return_value="Inject Skill")), # Main Menu
        MagicMock(ask=MagicMock(return_value="cursor")),       # Tool Selection
        MagicMock(ask=MagicMock(return_value="Global")),       # Location
        MagicMock(ask=MagicMock(return_value="Quit"))          # Main Menu (Loop 2)
    ]
    
    mock_questionary.confirm.return_value.ask.return_value = True

    try:
        interactive_mode()
    except SystemExit:
        pass
        
    mock_injector.inject.assert_called_once()
    assert "cursor" in str(mock_injector.inject.call_args[0][1])
