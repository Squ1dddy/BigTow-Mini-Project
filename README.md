# BigTow: trailer hire management system

A Python terminal application for managing trailer hire orders. Built during self-study, no dependencies beyond the standard library.

```
  ██████╗ ██╗ ██████╗     ████████╗ ██████╗ ██╗    ██╗
  ██╔══██╗██║██╔════╝        ██╔══╝██╔═══██╗██║    ██║
  ██████╔╝██║██║  ███╗       ██║   ██║   ██║██║ █╗ ██║
  ██╔══██╗██║██║   ██║       ██║   ██║   ██║██║███╗██║
  ██████╔╝██║╚██████╔╝       ██║   ╚██████╔╝╚███╔███╔╝
  ╚═════╝ ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚══╝╚══╝
  Trailer Hire System
```

## What it does

| Feature | Description |
|---------|-------------|
| Order processing | Configure trailer length, calculate cost per day, and generate a full order summary with a unique order ID |
| Customer management | Collect and save customer details, with surname-based lookup so returning customers are not re-entered |
| JSON persistence | Orders and customers are written to `orders.json` and `customers.json` and survive between sessions |
| Terminal UI | Banner, formatted output and screen clearing, all in the standard library |

## Pricing

Trailer width is fixed at 2.5m. Cost per day is the deck area at $125 per square metre, plus $100 per wheel set. Trailers under 3m take one wheel set, 3m and over take two.

```
cost_per_day = (length * 2.5 * 125) + (100 * wheel_sets)
```

A 5m trailer works out at 12.5 square metres, two wheel sets, $1762.50 a day.

## How it works

1. Pick **Place New Order**, enter a trailer length, and the system prices it
2. Enter the hire duration to get an order summary with a generated order ID
3. Customer details are collected and saved, and a returning customer can be found by surname
4. Everything is written back to the two JSON files

About 226 lines across 9 functions.

## Notes

The banner uses box-drawing characters. On Windows with a legacy console code page this raises a `UnicodeEncodeError`, so run it in a UTF-8 terminal, or set `PYTHONIOENCODING=utf-8`.

Order and customer IDs come from `random.randint(0, 999999)` with no uniqueness check. Over six-figure record counts that will eventually collide. Fine for a single-operator counter application, wrong for anything real.

## Running it

```bash
python main.py
```

## Getting the code

Clone it, or download a ZIP from the [releases page](https://github.com/Squ1dddy/bigtow-trailer-hire/releases).
