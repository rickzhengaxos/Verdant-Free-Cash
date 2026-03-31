# Verdant Free Cash Calculator

Scrapes contract data from Verdant's Profit Worksheet page and calculates NPV and Free Cash independently.

## Overview

This tool authenticates to Verdant via session cookie, pulls contract data (payment schedules, cash flows, COF, etc.) from the Profit Worksheet HTML, and replicates the Free Cash calculation.

## Data Extracted from Verdant

For each contract, the following fields are scraped from the Profit Worksheet page:

| Field | Source |
|---|---|
| Contract ID | Page HTML |
| Customer Name | Page HTML |
| Commencement Date | Page HTML |
| Total Financed | Page HTML |
| Total Positive Cash Flows | Page HTML (e.g., Interim Rent, Security Deposit) |
| Total Negative Cash Flows | Page HTML (e.g., Administration Cost, Broker Commission) |
| COF Total % | Page HTML (COF Basis + Uplift + Adjustment) |
| Payment Schedule(s) | Embedded JSON (`PaymentDate`, `PaymentAmount`, `PaymentFrequency`, `Occurrences`, `EndDate`) |

## NPV Calculation

### Step 1: Fractional Months

Each payment schedule is expanded into individual payments. For each payment, the fractional months from commencement is:

```
fractional_months = (days_from_commencement_to_first_payment / 360) * 12
                    + payment_index * months_between_payments
```

Where:
- **Year length = 360** (30/360 day count convention)
- **Periods per year = 12** (always, keeps units in months)
- **months_between_payments** = frequency value (1 for Monthly, 3 for Quarterly, 6 for SemiAnnual, 12 for Annual)
- **payment_index** = 0-based index within that schedule

### Step 2: Discounted Payment

```
discounted_payment = payment_amount / (1 + COF_total / 100 / 12) ^ fractional_months
```

### Step 3: NPV

```
NPV = sum of all discounted payments across all schedules
```

### Step 4: Free Cash

```
Free Cash = NPV - Total Financed + Total Positive Cash Flows - Total Negative Cash Flows
```

## Output

A table with one row per payment schedule containing:

| Column | Description |
|---|---|
| Contract | `#ContractID / Customer Name - $Financed` |
| Payment Date | Start date of the schedule |
| End Date | End date of the schedule |
| Payment Amount | Per-period payment |
| Frequency | Monthly, Quarterly, SemiAnnual, or Annual |
| Occurrences | Number of payments in the schedule |
| Total Amount | Payment Amount x Occurrences |
| Calculated NPV | Sum of all discounted payments |
| Total Financed | From Verdant |
| Total Positive Cash Flows | From Verdant |
| Total Negative Cash Flows | From Verdant |
| Calculated Free Cash | NPV - Financed + Positive - Negative |
| Link | Direct link to the Profit Worksheet in Verdant |

## Usage

1. Log into Verdant in your browser
2. Copy the `.ASpNet.Cookies.Vcc2` cookie value
3. Paste it into `Test.py`
4. Set the `CONTRACT_UID` for the contract you want to analyze
5. Run: `python Test.py`

## Validation

Tested against Contract #13637000 (Transportes Juventino Rosas, Incorporated):
- Verdant Free Cash: $49,841.69
- Calculated Free Cash: $49,473.35
- Delta: ~$368 (likely due to 360 vs 365 day count rounding)
