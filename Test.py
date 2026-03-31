import requests
import urllib3
import json
import re
import pandas as pd
import urllib.parse

urllib3.disable_warnings()

session = requests.Session()

# Paste your cookie value here
session.cookies.set(
    ".ASpNet.Cookies.Vcc2",
    "CfDJ8Fjj7v1EcOpLtu39cccO5jE031SOFYk7HBcMZKd-FNak99sGRtLSYWspYmierCoDbi0zxcfypJcQg6vqMkN2F38XlBA2980rSLTiZbBHASoJILPwV17MBRVlFxmc8kpksGf6FtExBvKhztoqsYD85d2mGL6c61OCMpdggI1F-JHxn9-Y4oTiz4kb0cQuNtj_M8Ee212T0cmTAMo1XmbYNg0VFRZ18PrcGncpPIPdX7BmPm-BVieCxV88sa5VtRgEzTG8nxpbcbV7KmrftL47HUqQRu9ylKmzVOUBAcPsVXArjbRhrLvwJolyazXupWj-Bbz8OCYT9nmvphyKDMK6n9z7aKiVnEX7Nhaiv_v7AxIJ-kRF5y3KmDgmfF3snYrxZGbbcyRzroa8HNWJ26JNDDK6QhK02KeWGTzKBwbNO7cMDM_giCUXcSo6JboVjRJRAXIYdzxmR5qHUVEwfeMaDw-VF3c-JlbAnIjY0QfbiE-76PEltxtKfLMJv2FBIzr5u65N2tr3CL6SIHnk2ZEcGvTyfA_GREyKVkXeLHrrrsUC7cZ6B6Aqpe10YwJpwYv_-etk9pgmuKJtBI-pgA6O9U9z3DXVz75wJVHRadHJDLNvfw3Jheh3Tl-cvMWwQyz2praesKoGYkP8Ju_gViDd3w9CsGph0hy91ClNFq5hX5VWI5ox44JAKykVSCHEZj0_jWRj1i7N9XKrCb-9lHLPNorNXrx2LNNtyq8jbUl-atOyxeXoqoDWXX5EZe3YJcdf2jUb_pwOcFV_9KkPIt3MAY8Ysa4QFMLklu2vyVsk-UBwYTooJMY4xIjX4Cl1KbXkCuAWGiDbh9zoEiLVaQmZhDKNQ0tfktc3evlQNtb_WXMZLJzoGKirtiQNriLeg-gP1-4KFxwfRMZq85ooiSxr6n_TAnF4UDev4rho9f7TfSawzY0U-jPT7qPf3eBTf0BNLJ_Ake9o80rQQUHucgIwWSsmJI_iHVGMhwUccO7VrZgvgmIbd2JEed2GsHJd6JEsM173k7AHeBgK3NaxKnL7EmY_r_ls5llzFTiGBrN05yUDmY_0Ui-WfNbjIjfOhNJTmbihbpWbAyxUzbEGEYBcmIqYmM9j8MisWfos_vxA5_SSTCWkk0GNgQRGpHrQwMywa7KsHRFSRS9xsW6q_B2gvcu2n6fOL3qcE7mmpNE3Tt8f_HLTePRJ3z_HpCwcTc7DndMbmw92fyU6Zbj3tku-vZmnUff5L0hfPETnzQVrAgaspxT8qo9zpYSp8Oh8-bkpxMjfvFPaasBwNoTCox5OhQyxlg1bKpb1IiqBjbv8USGWSwKcid_qMTSM6mENh4bez0AQ8JhaivZpu7m0Ov7El83BEre0tSduUSGH7pOKsoslkRnmwbxdl-l13sJEYCER-j5uWJaLffqdYuZGBnljAN-U2PTSE8blb9SvyFkDrKNCv-zG9RUpp8M4n9C5yphNbw8d_loyQZhmtm3VEL4Lb2nPPRk9DjAFp0MCjF-8Pbx_nT7GBRfcMlwtzFEvGbbs4--sL1BXZz0dyaGhzvHi8U8tdXfCtvFsj8fthVg8AbEHXhFy6Ml0_JUDO1NRKSEelfHoGWJHFSjKZbalAmF_8P1vaEvmh7L4XJBVL-HtvDeTi0SHkQCLAYAdfgHNTXbTthVQZ9D0QkTcSJwKugXAiTIwX8-dmDOn8yvWgN1d407so1tCb1OvGosoSNtYQns-h6vA6ajY3Q1rFqELcBZtWT7FbYAyTPR9vk-1PKxzY05tOEvn90CNDdMlqFDbC4tUSkDdcBEVl6OIbBKqE0KSKhPBfBP4oEXIqkt7_E841eTjs1r1SbKmVvXgwXANqZvdIPspvPxv3y6kpzTVkOa1zn2yFgOZBULWvYy96v_IUzWHVxFBYtBtE9Rsn3iCHz92kcKrxN_u1dVLntmRYB9KWlsgRalkGh6ns0fEWwgDKFf8CbBS34VhhD4qgZSX3eWo6dubp_lbkgpn0JqUv9TuHc3eJJ1PaIzf2DGLrFgZ5yBP9OvjHonKBb0Vx2jFlVAtiCy9EJ0U7ylYRMX4Du9bwvKI6U3VCJOH5TWVsB4tD9B26XL1KakyeEHx5PODrSyh6AEFObXpjOtWOtKd7D7QHwLp-3gVnpqcUnsXmgFB7JS1064jCPmrIf6Ey85NvhvdkEEh9RgsIw914FTzmbtAYA3aaZ0qRMDg_7cWKcozcoghll4cU6buHANRsy8Hldywipqlo1Bn1aJet4_ewbOn8LDcsYGxWdBIatYbzqJAv77A3lbtWH4QDftowJLq80ka35uxCnXjT2EqFY5_5i9KO-J2NveZqvTbOYAc3pKXzRQz9VB09X59DIHn9xMKuOkYV6zdWCV--d1LDLsb5amGVUhLsthvZb4TLUd2TKVEUX_p6PgD572EZyI6lSSjhMb9THOt98adR-a10d4aVvDD7TgoEHbpFK_V1lAcRysjt10UfCs01kArzEGmBG4UWQtrLCV1wDYaE21KN9oAmWp_eMY3fKGvGnFM5m6MjbuHl6wRbwZXvHkmKRoDrwBCNCWimMPnBkpGG-F1F_zwS0p77nOmOC0prEB6-SqGV2d02DkkYM6lDOKv1ROhXslm5ctOyyWyED9awmbPRIdPwlAR4K7OcMpT6CMDGwTtMfBwlU7aal-oNHaJhPpTI9qRLgYqA9UP1Z5gUxpDpwo3CKaqBx--hq-5N9lu_eBZ99HUs7RZxx3cw3grQFHITczodxLFAx3Hfdqg1UYg5xTr5J53JWntblBhThCG_BYeh84SGxCseTqFgSiEHwK4YBxeiG9B3UU-fNS1hOXiKFVM3PuNqSF6wpp2kToleKx2odJVP0tr5RqsAuWtl6ece8TVrd4_AY95d-34UgwdxrXsPcxeE1MzaGZEacRbs_wAf2me1Mupqt5HOh1t2VRnkIlj7jOv8Zx6jM4E-Nmd_OumqT29NPTwxnmgIglWNZ6rNcyQ7ehlTgtM31dTRXLc9MZYaXHdRENrfdYUE7s_KybJ_X180XaQXkxTX-emGOOdCvxYzkw_8MlczIyceRFOj--ORBDjV5YP0ux3LGAP-zRtmkFHgrWDysgWs2phhxvq6Y2Qv-5EDijz84g9rakReA3PLuvJCsihkW1Hv34TtR71SI80c08X_WbVgvMjMKjK5EFsCjsqZIca1KUil9yeHchhjekpe4T6xjMJoeM9IZB7PjAe0XhzLEFVTSsP4NPnRBotetq5tByXwBa1_wcac8jDAN67AV2m-PTVNGE3KONxJF-A6gArceGI3Vo17fjLMu5HPUH-Fe52-IQaMYTBYnFzJSQXIka0dXmnxvFTx8Mc7EoiztgOzSnAmMHyOeM9DtsnfjaNiU0Qnenb_3GqHZB9vMLEhmDwFe9Ulj2Vuv51qyGOa-kIa-7UbgkRvDV-2g8cYpB_NHya99vtGxm20f2dFghKNMCOfTZ4rpZtkzKUYq3maYHpS4s21_t8mf1PNQAO7aGcKWhlonUqjPf1bN1wUZwqSgUJ1oG5uP88Iry2tClN_V4wj5X39Pd-s2_vFOFkbP-b6uqZXv-iHXveTHTVB_FgQKLQ2jQ2TTAqjAQunUaUQcHFEVDK1H-Qt-T4hduemiYGhvKen7eh6tprQrmJsOrpOvmNC2Gw3j95Zxlfj2mSrmrQMZp9VsGO5FxLR8fYaWfe82uMjT22zfC93B1St6X3K9sI0Ym-M88EuMXQ2GOIeDXDft2DvYNTk3cA2KWve9J6aUdxAcZObA3FzEQYm1yphVVMPSoqiOc7GO8ECbMykWJBJkvA19HkBlDyorLJrz-OX2Yuy7BGI7Ku4s87YqJVJRByI-wcHGGpEVIr1kLmibfO_-keDx1fxV_MAKY4xEM0nSMsqsbb22B-GG0MrDI9aQ",
    domain="connect.verdantcc.com"
)

CONTRACT_UID = "9fd3eea4-c73c-41e4-a65b-24d674a01002"

# Fetch the Profit Worksheet page
response = session.get(
    f"https://connect.verdantcc.com/Contract/ProfitWorksheet?contractUID={CONTRACT_UID}",
    verify=False
)

html = response.text

# --- Helper to extract a dollar value next to a label ---
def extract_dollar(label, text):
    m = re.search(rf'{re.escape(label)}.*?\$([0-9,]+\.\d{{2}})', text, re.DOTALL)
    return m.group(1) if m else None

# --- Helper to extract a percentage next to a label ---
def extract_pct(label, text):
    m = re.search(rf'{re.escape(label)}.*?(\d+\.\d+%)', text, re.DOTALL)
    return m.group(1) if m else None

# --- Contract ID ---
contract_id_match = re.search(r'Contract ID.*?>([\d]+)<', html, re.DOTALL)
contract_id = contract_id_match.group(1) if contract_id_match else "N/A"

# --- Customer Name ---
customer_match = re.search(r'Customer Name.*?<a[^>]*>(.*?)<', html, re.DOTALL)
customer_name = customer_match.group(1) if customer_match else "N/A"

# --- Commencement Date ---
commence_match = re.search(r'Commencement Date.*?<span>([\d\\/]+)<', html, re.DOTALL)
commencement_date = commence_match.group(1).replace('\\/','/')  if commence_match else "N/A"

# --- Total Financed ---
total_financed = extract_dollar("Total Financed", html)

# --- Total Positive Cash Flows ---
total_positive = extract_dollar("Total Positive Cash Flows", html)

# --- Total Negative Cash Flows ---
total_negative = extract_dollar("Total Negative Cash Flows", html)

# --- COF Total ---
cof_total = extract_pct("COF Total", html)

# --- Payment Schedule ---
payment_json = re.search(
    r'payment-information-input-template.*?"Data":(\[.*?\]),"Total"',
    html,
    re.DOTALL
)
payments = json.loads(payment_json.group(1))

df = pd.DataFrame(payments)[["PaymentDate", "PaymentAmount", "PaymentFrequency", "Occurrences", "TotalAmount"]]

frequency_map = {1: "Monthly", 3: "Quarterly", 6: "SemiAnnual", 12: "Annual"}
df["PaymentFrequency"] = df["PaymentFrequency"].map(frequency_map)
df["PaymentDate"] = pd.to_datetime(df["PaymentDate"]).dt.strftime("%m/%d/%Y")
df["EndDate"] = pd.to_datetime([p["EndDate"] for p in payments]).strftime("%m/%d/%Y")

# --- Print Summary ---
print(f"Contract ID:              {contract_id}")
print(f"Commencement Date:        {commencement_date}")
print(f"Total Financed:           ${total_financed}")
print(f"Total Positive Cash Flows: ${total_positive}")
print(f"Total Negative Cash Flows: ${total_negative}")
print(f"COF Total:                {cof_total}")
print()
print("Payment Schedule:")
print(df.to_string(index=False))

# ============================================================
# NPV Calculation
# ============================================================
from datetime import datetime

commencement_dt = datetime.strptime(commencement_date, "%m/%d/%y")
cof_rate = float(cof_total.replace('%', ''))
year_length = 360
periods_per_year = 12

# Build schedule list from the raw payment JSON (supports N schedules)
schedules = []
for p in payments:
    freq = p['PaymentFrequency']  # 1=Monthly, 3=Quarterly, 6=SemiAnnual, 12=Annual
    schedules.append({
        'first_payment_date': pd.to_datetime(p['PaymentDate']).to_pydatetime(),
        'payment_amount': p['PaymentAmount'],
        'occurrences': p['Occurrences'],
        'months_between': freq,  # months between each payment
    })

# Expand every individual payment, compute fractional months & discounted value
rows = []
payment_number = 1
cum_terms = 0

for sched in schedules:
    days_diff = (sched['first_payment_date'] - commencement_dt).days

    for i in range(sched['occurrences']):
        frac_months = (days_diff / year_length) * periods_per_year + i * sched['months_between']
        disc_payment = sched['payment_amount'] / ((1 + cof_rate / 100 / 12) ** frac_months)

        rows.append({
            'PaymentNumber': payment_number,
            'PaymentAmount': sched['payment_amount'],
            'FractionalMonths': round(frac_months, 6),
            'DiscountedPayment': round(disc_payment, 2),
        })
        payment_number += 1

    cum_terms += sched['occurrences']

npv_df = pd.DataFrame(rows)
npv = npv_df['DiscountedPayment'].sum()

# ============================================================
# Free Cash Calculation
# ============================================================
financed = float(total_financed.replace(',', ''))
pos_cf = float(total_positive.replace(',', ''))
neg_cf = float(total_negative.replace(',', ''))
free_cash = npv - financed + pos_cf - neg_cf

# ============================================================
# Build Profit Worksheet Link
# ============================================================
nav_json = json.dumps([{"t": f"Contract+{contract_id}", "l": f"/Contract/Summary/{CONTRACT_UID}"}], separators=(',', ':'))
nav_encoded = urllib.parse.quote(urllib.parse.quote(nav_json, safe=''), safe='')
link = f"https://connect.verdantcc.com/Contract/ProfitWorksheet?contractUID={CONTRACT_UID}&nav={nav_encoded}"

# ============================================================
# Summary Table
# ============================================================
contract_label = f"#{contract_id} / {customer_name} - ${total_financed}"

# Build one row per payment schedule
summary_rows = []
for i, p in enumerate(payments):
    freq_label = frequency_map[p['PaymentFrequency']]
    summary_rows.append({
        'Contract': contract_label,
        'Payment Date': pd.to_datetime(p['PaymentDate']).strftime("%m/%d/%Y"),
        'End Date': pd.to_datetime(p['EndDate']).strftime("%m/%d/%Y"),
        'Payment Amount': f"${p['PaymentAmount']:,.2f}",
        'Frequency': freq_label,
        'Occurrences': p['Occurrences'],
        'Total Amount': f"${p['TotalAmount']:,.2f}",
        'Calculated NPV': f"${npv:,.2f}",
        'Total Financed': f"${financed:,.2f}",
        'Total Positive Cash Flows': f"${pos_cf:,.2f}",
        'Total Negative Cash Flows': f"${neg_cf:,.2f}",
        'Calculated Free Cash': f"${free_cash:,.2f}",
        'Link': link,
    })

summary = pd.DataFrame(summary_rows)

print()
print(summary.to_string(index=False))