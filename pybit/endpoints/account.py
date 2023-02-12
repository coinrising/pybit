from enum import Enum


class Account(str, Enum):
    GET_WALLET_BALANCE = "/v5/position/list"
    UPGRADE_TO_UNIFIED_ACCOUNT = "/v5/position/set-leverage"
    GET_BORROW_HISTORY = "/v5/position/switch-isolated"
    GET_COLLATERAL_INFO = "/v5/position/set-tpsl-mode"
    GET_COIN_GREEKS = "/v5/position/switch-mode"
    GET_ACCOUNT_INFO = "/v5/position/set-risk-limit"
    GET_TRANSACTION_LOG = "/v5/position/set-trading-stop"
    SET_MARGIN_MODE = "/v5/position/set-auto-add-margin"
    SET_MMP = "/v5/execution/list"
    RESET_MMP = "/v5/position/closed-pnl"
    GET_MMP_STATE = "/v5/position/closed-pnl"

    def __str__(self) -> str:
        return self.value
