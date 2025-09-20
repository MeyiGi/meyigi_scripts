import os
import shutil
import pytest

from playwright.async_api import Page
from meyigi_scripts import PlaywrightUndetected


@pytest.mark.asyncio
async def test_init_creates_profile_dir(tmp_path, monkeypatch):
    """Test that initializing PlaywrightUndetected creates the profile directory"""
    # Redirect BASE_PROFILE_DIR to tmp_path
    base = tmp_path / "data" / "playwright_profiles_no_proxy"
    monkeypatch.setenv("BASE_PROFILE_DIR", str(base))
    
    inst = PlaywrightUndetected()
    
    # Profile dir should exist immediately after init
    assert os.path.isdir(inst.profile_path)
    # It should be under our tmp_path base
    assert str(inst.profile_path).startswith(str(base))
    
    # Clean up the instance to avoid resource warnings
    await inst.stop()


@pytest.mark.asyncio
async def test_start_returns_page_and_navigation(tmp_path, monkeypatch):
    """Test that start() returns a Page and can navigate"""
    # Ensure data and downloads go to tmp dirs
    monkeypatch.setenv("BASE_PROFILE_DIR", str(tmp_path / "profiles"))
    
    inst = PlaywrightUndetected()
    page: Page = await inst.start()
    
    assert isinstance(page, Page)
    
    # Navigate to a simple in-memory page
    await page.goto("data:text/html,<title>pytest</title>")
    assert await page.title() == "pytest"
    
    # Clean up
    await inst.stop()


@pytest.mark.asyncio
async def test_stop_cleans_profile(tmp_path, monkeypatch):
    """Test that stop() cleans up the profile directory"""
    monkeypatch.setenv("BASE_PROFILE_DIR", str(tmp_path / "profiles"))
    
    inst = PlaywrightUndetected()
    prof = inst.profile_path
    
    assert os.path.isdir(prof)
    
    await inst.start()
    await inst.stop()
    
    # After stop, profile dir should be removed
    assert not os.path.exists(prof)


@pytest.mark.asyncio
async def test_get_desktop_user_agent():
    """Test that _get_desktop_user_agent returns a desktop user agent"""
    inst = PlaywrightUndetected()
    ua = inst._get_desktop_user_agent()
    
    # Should not contain mobile indicators
    mobile_indicators = ["Mobile", "iPhone", "Android"]
    assert not any(indicator in ua for indicator in mobile_indicators)
    
    # Should contain Chrome indicators
    assert "Chrome" in ua
    assert "Safari" in ua
    
    # Clean up
    await inst.stop()


@pytest.mark.skip(reason="Requires a local server to test real downloads")
@pytest.mark.asyncio
async def test_handle_download(tmp_path, monkeypatch):
    """
    Test download handling functionality.
    
    To implement this test, you would need to:
    - Set up a local HTTP server serving a test file
    - Navigate to that URL and trigger a download
    - Assert the file appears in DOWNLOADS_DIR
    """
    pass