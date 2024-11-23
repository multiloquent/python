import pytest
from television import Television


@pytest.fixture
def tv():
    return Television()


def test_power_on(tv):
    """Test the power method and check TV details when on."""
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # TV should be on with default values


def test_power_off(tv):
    """Test the power method and check TV details when off."""
    tv.power()  # Turn it on first
    tv.power()  # Then turn it off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # TV should be off with default values


def test_mute_on_and_muted(tv):
    """Test mute method when TV is on and muted."""
    tv.power()  # Turn on TV
    tv.volume_up()  # Increase volume
    tv.mute()  # Mute the TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Volume should be 0 (muted)


def test_unmute(tv):
    """Test un-mute method when TV is un-muted."""
    tv.power()  # Turn on TV
    tv.volume_up()  # Increase volume
    tv.mute()  # Mute the TV
    tv.mute()  # Unmute the TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Volume should be restored to previous


def test_mute_when_off(tv):
    """Test mute when the TV is off."""
    tv.mute()  # Try to mute the TV when it's off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # TV should remain off, volume still 0


def test_channel_up(tv):
    """Test the channel_up method."""
    tv.power()  # Turn on TV
    tv.channel_up()  # Increase channel
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"  # Channel should increase by 1


def test_channel_up_max(tv):
    """Test channel_up method when channel reaches maximum."""
    tv.power()  # Turn on TV
    for _ in range(4):  # Channel should loop back after max
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Should loop to min channel after max


def test_channel_down(tv):
    """Test the channel_down method."""
    tv.power()  # Turn on TV
    tv.channel_down()  # Decrease channel
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Channel should go to the max (3)


def test_channel_down_min(tv):
    """Test channel_down method when channel reaches minimum."""
    tv.power()  # Turn on TV
    tv.channel_down()  # Decrease channel (wrap to max)
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Should wrap back to max


def test_volume_up(tv):
    """Test the volume_up method."""
    tv.power()  # Turn on TV
    tv.volume_up()  # Increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Volume should increase by 1


def test_volume_up_max(tv):
    """Test volume_up method when volume reaches maximum."""
    tv.power()  # Turn on TV
    tv.volume_up()  # Increase volume to max
    tv.volume_up()  # Try increasing beyond max
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"  # Should stay at max volume


def test_volume_down(tv):
    """Test the volume_down method."""
    tv.power()  # Turn on TV
    tv.volume_up()  # Increase volume to max first
    tv.volume_up()
    tv.volume_down()  # Decrease volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Volume should decrease by 1


def test_volume_down_min(tv):
    """Test volume_down method when volume reaches minimum."""
    tv.power()  # Turn on TV
    tv.volume_down()  # Try decreasing volume from min (nothing should happen)
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Volume should remain at min


def test_volume_up_when_muted(tv):
    """Test volume_up method when TV is muted."""
    tv.power()  # Turn on TV
    tv.mute()  # Mute the TV
    tv.volume_up()  # Try increasing volume while muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Should unmute and increase volume to 1


def test_volume_down_when_muted(tv):
    """Test volume_down method when TV is muted."""
    tv.power()  # Turn on TV
    tv.mute()  # Mute the TV
    tv.volume_down()  # Try decreasing volume while muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Volume should remain at 0 (muted)
