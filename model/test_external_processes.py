import pytest
import datetime

from model.external_processes import create_market_price_process

def test_market_price_process():
    date_start = datetime.datetime(2021, 1, 1)
    dt = 225 # that's 225 epochs in a day
    timesteps = 5 # our simulation range will be 5 days (with the above `dt`)

    p = create_market_price_process(date_start, dt=dt, timesteps=timesteps)

    assert p(0, 0) == 737.71 # Day 0 (timesteps 0..224)
    assert p(0, 50) == 737.71 # Day 0 (timesteps 0..224)
    assert p(0, 225) == 730.4 # Day 1 (225..*)

    # Maximum range that our 'p' function can return
    # given parameters used to construct it
    assert p(0, dt*timesteps - 1) == 1041.50

    with pytest.raises(Exception) as ex:
        p(0, dt*timesteps)

    assert ex.match(r"out of bounds")

