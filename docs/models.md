# OMTrader Models Documentation

## Table of Contents
- [Order Model](#order-model)
- [Position Model](#position-model)
- [Deal Model](#deal-model)
- [Trade Account Model](#trade-account-model)
- [Symbol Model](#symbol-model)
- [History Tick Model](#history-tick-model)
- [HTTP Response Model](#http-response-model)

## Order Model
[↑ Back to Table of Contents](#table-of-contents)

The `ModelOrder` class represents an order in the trading system.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | int | Order ID |
| account_id | int | Account ID |
| symbol_id | int | Symbol ID |
| status | ModelOrderStatus | Order status |
| type | ModelOrderType | Order type |
| side | ModelSideType | Order side (Buy/Sell) |
| volume_initial | float | Initial order volume |
| volume_current | float | Current order volume |
| price_order | float | Order price |
| price_sl | float | Stop loss price |
| price_tp | float | Take profit price |
| price_trigger | float | Trigger price |
| price_current | float | Current market price |
| comment | str | Order comment |
| external_id | str | ID of position on LP |
| created_at | str | Creation timestamp |
| updated_at | str | Last update timestamp |
| time_setup | str | Setup timestamp |
| time_expiration | str | Expiration timestamp |
| time_done | str | Completion timestamp |
| expiration_policy | ModelExpirationPolicy | Expiration policy |
| type_fill | ModelFillPolicy | Fill policy |
| reason | ModelReasonType | Order reason |
| digits | int | Configured digits for this order |
| digits_currency | int | Currency digits |
| contract_size | float | Contract size |
| rate_margin | float | Margin rate |

### Relationships
- `account`: ModelTradeAccount - Associated trading account
- `position`: ModelPosition - Associated position
- `symbol`: ModelSymbol - Associated trading symbol

## Position Model
[↑ Back to Table of Contents](#table-of-contents)

The `ModelPosition` class represents a trading position.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | int | Position ID |
| account_id | int | Account ID |
| symbol_id | int | Symbol ID |
| status | ModelPositionStatus | Position status |
| side | ModelSideType | Position side (Long/Short) |
| volume_initial | float | Initial position volume (lots) |
| volume_current | float | Current position volume (lots) |
| price_open | float | Opening price |
| price_current | float | Current market price |
| price_sl | float | Stop loss price |
| price_tp | float | Take profit price |
| profit | float | Current profit |
| total_profit | float | Total profit including swaps and commission |
| swaps | float | Swap fees |
| commission | float | Commission fees |
| comment | str | Position comment |
| external_id | str | ID of position on LP |
| created_at | str | Creation timestamp |
| updated_at | str | Last update timestamp |
| exit_level | ModelExitLevel | When to exit (overrides S/L) |
| exit_loos | float | Exit loss value |
| exit_profit | float | Exit profit value |
| digits | int | Configured digits for this position |
| digits_currency | int | Currency digits |
| contract_size | float | Contract size |
| rate_margin | float | Margin rate |
| rate_profit | float | Profit rate |
| storage | float | Storage fees |

### Relationships
- `account`: ModelTradeAccount - Associated trading account
- `deals`: List[ModelDeal] - Associated deals
- `symbol`: ModelSymbol - Associated trading symbol

## Deal Model
[↑ Back to Table of Contents](#table-of-contents)

The `ModelDeal` class represents a completed trade deal.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | int | Deal ID |
| account_id | int | Account ID |
| order_id | int | Associated order ID |
| position_id | int | Associated position ID |
| symbol_id | int | Symbol ID |
| side | ModelSideType | Deal side (Buy/Sell) |
| direction | ModelDirectionType | Deal direction |
| volume | float | Deal volume (lots) |
| price | float | Deal execution price |
| profit | float | Deal profit |
| profit_raw | float | Raw profit before fees |
| commission | float | Commission fees |
| swap | float | Swap fees |
| fee | float | Additional fees |
| storage | float | Storage fees |
| closed_volume | float | Partially closed volume |
| external_id | str | ID of position on LP |
| external_volume | float | Volume on LP |
| external_volume_closed | float | Closed volume on LP |
| market_bid | float | Market bid price |
| market_ask | float | Market ask price |
| market_last | float | Last market price |
| comment | str | Deal comment |
| created_at | str | Creation timestamp |
| updated_at | str | Last update timestamp |
| channel | ModelChannelType | Deal channel |
| digits | int | Configured digits |
| digits_currency | int | Currency digits |
| contract_size | float | Contract size |
| tick_size | float | Symbol tick size |
| tick_value | float | Symbol tick value |

### Relationships
- `account`: ModelTradeAccount - Associated trading account
- `symbol`: ModelSymbol - Associated trading symbol

## Trade Account Model
[↑ Back to Table of Contents](#table-of-contents)

The `ModelTradeAccount` class represents a trading account.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | int | Account ID |
| user_id | int | User ID |
| client_id | int | Client ID |
| group_id | int | Group ID |
| currency | str | Account currency |
| currency_digits | int | Currency decimal places |
| balance | float | Account balance |
| credit | float | Account credit |
| equity | float | Account equity |
| margin | float | Used margin |
| margin_free | float | Free margin |
| margin_level | float | Margin level percentage |
| margin_initial | float | Initial margin |
| margin_maintenance | float | Maintenance margin |
| margin_leverage | float | Account leverage |
| profit | float | Current profit |
| storage | float | Storage fees |
| floating | float | Floating P/L |
| assets | float | Total assets |
| liabilities | float | Total liabilities |
| blocked_commission | float | Blocked commission |
| blocked_profit | float | Blocked profit |
| day_profit | float | Day's profit |
| week_profit | float | Week's profit |
| month_profit | float | Month's profit |
| leverage | int | Account leverage (1:x where x=5000 down to 1) |
| trade_type | ModelTradeType | Account trading properties |
| liqudation_status | ModelLiqudationStatus | Account liquidation status |
| enable_risk_management | bool | Enable account-level P/L control |
| max_day_loss | float | Maximum daily loss limit |
| max_day_profit | float | Maximum daily profit limit |
| max_week_loss | float | Maximum weekly loss limit |
| max_week_profit | float | Maximum weekly profit limit |
| max_month_loss | float | Maximum monthly loss limit |
| max_month_profit | float | Maximum monthly profit limit |

### Relationships
- `orders`: List[ModelOrder] - Account orders
- `positions`: List[ModelPosition] - Account positions
- `deals`: List[ModelDeal] - Account deals
- `user`: Dict[str, Any] - Associated user information

## Symbol Model
[↑ Back to Table of Contents](#table-of-contents)

The `MessagingViewSymbol` class represents a trading symbol.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| id | int | Symbol ID |
| symbol | str | Symbol name |
| base_currency | str | Base currency |
| quote_currency | str | Quote currency |
| digits | int | Price decimal places |
| contract_size | float | Contract size |
| spread | int | Spread in points |
| spread_balance | int | Spread balance |
| status | ModelSymbolStatus | Symbol status |
| enabled | bool | Whether symbol is enabled |
| margin_initial | float | Initial margin requirement |
| margin_maintenance | float | Maintenance margin requirement |
| margin_buy | float | Buy margin requirement |
| margin_sell | float | Sell margin requirement |
| swap_long | float | Long position swap rate |
| swap_short | float | Short position swap rate |
| swap_type | ModelSwaptype | Swap calculation type |
| swaps_enabled | bool | Whether swaps are enabled |
| broker_fee | float | Broker fee |
| maker_fee | float | Maker fee |
| step | float | Minimum price movement |
| min_value | float | Minimum order value |
| max_value | float | Maximum order value |
| stop_level | int | Stop level in points |
| execution | ModelExecutionMode | Execution mode |
| filling | ModelFillPolicy | Fill policy |
| calculation | ModelCalcType | Price calculation type |
| trade_level | ModelTradeLevel | Trading level |
| symbol_class | ModelSymbolClass | Symbol class |

## History Tick Model
[↑ Back to Table of Contents](#table-of-contents)

The `MessagingHistoryTick` class represents a historical price tick.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| time | int | Tick timestamp |
| open | float | Opening price |
| high | float | Highest price |
| low | float | Lowest price |
| close | float | Closing price |
| volume | float | Trading volume |

## HTTP Response Model
[↑ Back to Table of Contents](#table-of-contents)

The `HttpHttpResponse` class represents an HTTP response from the API.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| code | int | HTTP status code |
| success | bool | Whether the request was successful |
| data | Dict[str, Any] \| List[Any] \| str | Response data if successful |
| error | str | Generic error message |
| message | str | Detailed error message |