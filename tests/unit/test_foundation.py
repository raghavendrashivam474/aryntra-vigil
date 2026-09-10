from vigil import __version__
from vigil.core import VigilSystem

def test_package_version() -> None:
    """Verify that the package exposes the correct development version."""
    assert __version__ == "0.1.0"

def test_vigil_system_initialization() -> None:
    """Verify that the VIGIL system can initialize with minimal ready status."""
    system = VigilSystem()
    status = system.get_status()
    
    assert status["initialized"] is True
    assert status["status"] == "READY"
    assert status["identity"] == "Aryntra VIGIL"
    assert status["version"] == "0.1.0"
