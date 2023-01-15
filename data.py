import pandas as pd
import numpy as np
from clickhouse_driver import Client
from web3 import Web3

from config import CONFIG


def get_default_data() -> tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
    quotes_df = pd.DataFrame(
        {
            "block_number": np.arange(11000000, 16400000, 1000),
            "eth_quote": np.ones_like(np.arange(11000000, 16400000, 1000)),
        }
    )

    pnl_df = pd.DataFrame(
        {
            "block_number": np.arange(11000000, 16400000, 1000),
            "pnl": np.ones_like(np.arange(11000000, 16400000, 1000)),
        }
    )

    return quotes_df, pnl_df, [], [], "NOT DEFINED"


def get_data(
    token_address: str,
    wallet_address: str,
) -> tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
    """
    The function extracts data from clickhouse database and constructs
    1. pd.DataFrame `quotes_df`
    2. pd.DataFrame `pnl_df`
    3. list[int] of block numbers of all `in_transfers` to `wallet_address`
    4. list[int] of block numbers of all `out_transfers` from `wallet_address`
    5. token symbol of `token_address`

    What you should do is to implement the function.

    You need to extract data from clickhouse database via sql queries
    ```
    client.execute(f"SELECT ... FROM ... WHERE ... LIMIT {CONFIG.limit_rows}")
    ```
    It is reasonable to LIMIT your sql query with predefined number of rows to prevent both
    server's and your PC's overload.

    When selecting from quotes table use the following query
    ```
    client.execute(f"SELECT ... FROM quotes WHERE block_number % 100 = 0 LIMIT {CONFIG.limit_rows}")
    ```
    and fill the interim values with the last left value. For instance, the quote for all the blocks
    in [16000500, 16000599] is assigned to the quote of 16000500 block.

    Args:
        token_address (str): token address
        wallet_address (str): wallet_address

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, list[int], list[int], str]:
            tuple(quotes_df, pnl_df, in_transers, out_transfers, token_symbol)
    """

    client = Client.from_url(CONFIG.clickhouse_url)
    w3 = Web3(Web3.HTTPProvider(CONFIG.provider_uri))

    # YOUR CODE GOES HERE

    # quotes_df = ...
    # pnl_df = ...
    # in_transers = ...
    # out_transfers = ...
    # token_symbol = ...

    # Uncomment the line below and delete `return get_default_data()`
    # return quotes_df, pnl_df, in_transers, out_transfers, token_symbol
    return get_default_data()
