import pandas as pd
# Import calculations module.
from src.include.calculations import calculate_daily_returns
from src.include.profiler import get_value

# Test Pandas DataFrame instance.
sample_data = {
    "A" : [1, 2, 3],
    "B" : [2, 3, 4],
    "C" : [3, 4, 5]
}
sample_df = pd.DataFrame(sample_data)

def test_calculate_daily_returns():
    assert calculate_daily_returns(sample_df) == sample_df.pct_change().dropna()