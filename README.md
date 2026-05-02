# BigTow — Trailer Hire Management System

A Python terminal application for managing trailer hire orders, built as a mini-project during self-study.

---

## What It Does

| Feature | Description |
|---------|-------------|
| Order Processing | Configure trailer length, calculate cost per day, and generate a full order summary |
| Customer Management | Collect and save customer details, with surname-based lookup for returning customers |
| JSON Persistence | Orders and customers are saved to local JSON files and persist between sessions |
| ASCII UI | Clean terminal interface with a branded banner and formatted output |

---

## How It Works

1. Select **Place New Order** to configure a trailer and calculate hire cost
2. Enter hire duration to generate an order summary with a unique order ID
3. Customer details are collected and saved — returning customers can be looked up by surname
4. All orders and customer records are written to `orders.json` and `customers.json`

---

## Pricing Formula

- Trailer width is fixed at 2.5m
- Cost per day = `(length × 2.5 × $125) + wheel set cost`
- Trailers under 3m use 1 wheel set, 3m and over use 2

---

## Skills Demonstrated

- Python fundamentals and control flow
- JSON file I/O and data persistence
- Input validation and error handling
- Terminal UI design and formatting

---

## Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,vscode,git" />
</p>
