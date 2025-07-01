import os
import shutil
import tempfile
import pytest

from playwright.sync_api import Page
from meyigi_scripts import PlaywrightUndetected

@pytest.fixture(autouse=True)
def cleanup_downloads(tmp_path, monkeypatch):
    # Redirect downloads to a temp dir
    downloads = tmp_path / "downloads"
    monkeypatch.setenv("PWD", str(tmp_path))  # so DOWNLOADS_DIR = tmp_path/downloads
    yield
    # cleanup after test
    if downloads.exists():
        shutil.rmtree(downloads)

def test_init_creates_profile_dir(tmp_path, monkeypatch):
    # Redirect BASE_PROFILE_DIR to tmp_path/data/playwright_profiles_no_proxy
    base = tmp_path / "data" / "playwright_profiles_no_proxy"
    monkeypatch.setenv("BASE_PROFILE_DIR", str(base))
    inst = PlaywrightUndetected()
    # Profile dir should exist immediately after init
    assert os.path.isdir(inst.profile_path)
    # It should be under our tmp_path base
    assert str(inst.profile_path).startswith(str(base))

def test_start_returns_page_and_navigation(tmp_path, monkeypatch):
    # Ensure data and downloads go to tmp dirs
    monkeypatch.setenv("BASE_PROFILE_DIR", str(tmp_path / "profiles"))
    monkeypatch.setenv("PWD", str(tmp_path))

    inst = PlaywrightUndetected()
    page: Page = inst.start()
    assert isinstance(page, Page)
    # Navigate to a simple in-memory page
    page.goto("data:text/html,<title>pytest</title>")
    assert page.title() == "pytest"
    # Clean up
    inst.stop()

def test_stop_cleans_profile(tmp_path, monkeypatch):
    monkeypatch.setenv("BASE_PROFILE_DIR", str(tmp_path / "profiles"))
    inst = PlaywrightUndetected()
    prof = inst.profile_path
    assert os.path.isdir(prof)
    inst.start()
    inst.stop()
    # After stop, profile dir should be removed
    assert not os.path.exists(prof)

# Optional: a placeholder for download tests
@pytest.mark.skip(reason="Requires a local server to test real downloads")
def test_handle_download(tmp_path, monkeypatch):
    """
    You can:
      - spin up http.server serving a small file
      - page.goto() to that URL
      - trigger a click/download
      - then assert file in DOWNLOADS_DIR
    """
    pass