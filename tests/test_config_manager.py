
import pytest
from pathlib import Path
from saki.core.config_manager import ConfigManager

@pytest.fixture
def temp_config_dir(tmp_path):
    # Mock home directory logic by overriding ConfigManager paths
    config_dir = tmp_path / ".saki"
    return config_dir

def test_config_defaults(temp_config_dir):
    # Subclass or mock to override init
    class TestConfigManager(ConfigManager):
        def __init__(self):
            self.config_dir = temp_config_dir
            self.config_file = self.config_dir / "config.yaml"
            self._config = {}
            self.load()

    cm = TestConfigManager()
    assert cm.get_repositories()[0]["name"] == "official"
    assert "antigravity" in cm.get_all_tools()

def test_add_repository(temp_config_dir):
    class TestConfigManager(ConfigManager):
        def __init__(self):
            self.config_dir = temp_config_dir
            self.config_file = self.config_dir / "config.yaml"
            self._config = {}
            self.load()

    cm = TestConfigManager()
    cm.add_repository("test-repo", "https://git.example.com", "git")
    
    repos = cm.get_repositories()
    assert len(repos) == 2 # Default + New
    assert repos[-1]["name"] == "test-repo"
    assert repos[-1]["url"] == "https://git.example.com"

def test_remove_repository(temp_config_dir):
    class TestConfigManager(ConfigManager):
        def __init__(self):
            self.config_dir = temp_config_dir
            self.config_file = self.config_dir / "config.yaml"
            self._config = {}
            self.load()

    cm = TestConfigManager()
    cm.add_repository("test-repo", "https://git.test", "git")
    cm.remove_repository("test-repo")
    
    repos = cm.get_repositories()
    assert len(repos) == 1
    assert repos[0]["name"] == "official"
