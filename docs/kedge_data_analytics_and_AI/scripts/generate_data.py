import math
import random
from datetime import date, timedelta
from pathlib import Path

import polars as pl

SEED = 42
OUTPUT_DIR = Path("docs/kedge_data_analytics_and_AI/data")
START_DATE = date(2025, 1, 1)
END_DATE = date(2025, 12, 31)
N_CUSTOMERS = 1_000
N_PRODUCTS = 30
N_SALES = 6_000
N_CAMPAIGN_SENDS = 7_000
N_REVIEWS = 2_500
N_WEBSITE_VISITS = 10_000

CATEGORIES = ["Skincare", "Fitness", "Home", "Accessories", "Wellness"]

TRAFFIC_SOURCES = [
    "organic_search",
    "paid_search",
    "social",
    "email",
    "direct",
    "referral",
]

TRAFFIC_SOURCE_WEIGHTS = [0.27, 0.19, 0.18, 0.14, 0.16, 0.06]
CUSTOMER_SEGMENTS = ["Value", "Regular", "Premium"]
CUSTOMER_SEGMENT_WEIGHTS = [0.35, 0.48, 0.17]

CAMPAIGNS = [
    {
        "campaign_id": "CMP01",
        "campaign_name": "New Year Reset",
        "channel": "email",
        "message": "Start fresh with practical favorites.",
        "start_month": 1,
        "end_month": 2,
    },
    {
        "campaign_id": "CMP02",
        "campaign_name": "Spring Refresh",
        "channel": "ads",
        "message": "Refresh your routine for spring.",
        "start_month": 3,
        "end_month": 4,
    },
    {
        "campaign_id": "CMP03",
        "campaign_name": "Member Picks",
        "channel": "email",
        "message": "Popular picks selected for you.",
        "start_month": 5,
        "end_month": 6,
    },
    {
        "campaign_id": "CMP04",
        "campaign_name": "Summer Essentials",
        "channel": "ads",
        "message": "Simple essentials for warmer days.",
        "start_month": 6,
        "end_month": 8,
    },
    {
        "campaign_id": "CMP05",
        "campaign_name": "Back to Routine",
        "channel": "email",
        "message": "Get back into your everyday rhythm.",
        "start_month": 8,
        "end_month": 9,
    },
    {
        "campaign_id": "CMP06",
        "campaign_name": "Autumn Edit",
        "channel": "ads",
        "message": "Discover this season's useful upgrades.",
        "start_month": 9,
        "end_month": 10,
    },
    {
        "campaign_id": "CMP07",
        "campaign_name": "Early Holiday",
        "channel": "email",
        "message": "A head start on thoughtful gifting.",
        "start_month": 11,
        "end_month": 11,
    },
    {
        "campaign_id": "CMP08",
        "campaign_name": "Holiday Highlights",
        "channel": "ads",
        "message": "Explore customer favorites this holiday.",
        "start_month": 11,
        "end_month": 12,
    },
]


rng = random.Random(SEED)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TOTAL_DAYS = (END_DATE - START_DATE).days + 1


def logistic(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def random_date() -> date:
    return START_DATE + timedelta(days=rng.randrange(TOTAL_DAYS))


def random_date_between_months(start_month: int, end_month: int) -> date:
    valid_dates = []

    for i in range(TOTAL_DAYS):
        d = START_DATE + timedelta(days=i)

        if start_month <= d.month <= end_month:
            valid_dates.append(d)

    return rng.choice(valid_dates)


def seasonal_multiplier(d: date) -> float:
    yearly_wave = 0.06 * math.sin(2 * math.pi * (d.timetuple().tm_yday - 220) / 365)

    holiday_effect = 0.08 if d.month in (11, 12) else 0

    return 1 + yearly_wave + holiday_effect


customers = []
for i in range(1, N_CUSTOMERS + 1):
    segment = rng.choices(CUSTOMER_SEGMENTS, weights=CUSTOMER_SEGMENT_WEIGHTS, k=1)[0]
    customers.append(
        {
            "customer_id": f"C{i:05d}",
            "segment": segment,
            "engagement": rng.uniform(-0.7, 0.7),
            "price_sensitivity": rng.uniform(-0.6, 0.6),
        }
    )
customers_by_id = {customer["customer_id"]: customer for customer in customers}
customer_ids = list(customers_by_id)


product_adjectives = [
    "Daily",
    "Pure",
    "Urban",
    "Essential",
    "Bright",
    "Active",
    "Calm",
    "Modern",
]
product_nouns = ["Serum", "Bottle", "Mat", "Lamp", "Bag", "Cream", "Band", "Organizer"]

products = []
for i in range(1, N_PRODUCTS + 1):
    category = CATEGORIES[(i - 1) % len(CATEGORIES)]
    adjective = product_adjectives[(i - 1) % len(product_adjectives)]
    noun = product_nouns[(i * 3) % len(product_nouns)]
    products.append(
        {
            "product_id": f"P{i:03d}",
            "product_name": f"{adjective} {noun} {i:02d}",
            "category": category,
            "base_price": round(rng.uniform(12, 110), 2),
            "quality": rng.uniform(-0.5, 0.5),
            "popularity": rng.uniform(0.75, 1.25),
        }
    )

product_weights = [product["popularity"] for product in products]


sales_rows = []
for i in range(1, N_SALES + 1):
    d = random_date()
    customer_id = rng.choice(customer_ids)
    customer = customers_by_id[customer_id]
    product = rng.choices(products, weights=product_weights, k=1)[0]
    quantity_weights = [0.70, 0.21, 0.07, 0.02]
    if customer["segment"] == "Premium":
        quantity_weights = [0.64, 0.24, 0.09, 0.03]
    quantity = rng.choices([1, 2, 3, 4], weights=quantity_weights, k=1)[0]
    discount = rng.choices(
        [0, 0.05, 0.10, 0.15], weights=[0.67, 0.16, 0.12, 0.05], k=1
    )[0]

    seasonal_price_effect = 1 + (seasonal_multiplier(d) - 1) * 0.15
    unit_price = (
        product["base_price"]
        * (1 - discount)
        * seasonal_price_effect
        * rng.uniform(0.98, 1.02)
    )
    unit_price = round(unit_price, 2)
    sales_rows.append(
        {
            "transaction_id": f"T{i:06d}",
            "customer_id": customer_id,
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "quantity": quantity,
            "unit_price": unit_price,
            "transaction_total": round(
                quantity * unit_price,
                2,
            ),
            "date": d,
        }
    )

sales_df = pl.DataFrame(sales_rows)

campaign_rows = []
for i in range(1, N_CAMPAIGN_SENDS + 1):
    customer_id = rng.choice(customer_ids)
    customer = customers_by_id[customer_id]
    campaign = rng.choice(CAMPAIGNS)
    sent_date = random_date_between_months(
        campaign["start_month"], campaign["end_month"]
    )
    click_score = (
        -2.1
        + 0.55 * customer["engagement"]
        + (0.20 if campaign["channel"] == "email" else 0)
        + (0.15 if sent_date.month in (11, 12) else 0)
        + rng.uniform(-0.15, 0.15)
    )
    clicked = rng.random() < logistic(click_score)
    purchase_score = (
        -3.0
        + 0.50 * customer["engagement"]
        + (1.25 if clicked else 0)
        + (0.15 if sent_date.month in (11, 12) else 0)
        + rng.uniform(-0.15, 0.15)
    )
    purchased = rng.random() < logistic(purchase_score)
    campaign_rows.append(
        {
            "send_id": f"SEND{i:06d}",
            "campaign_id": campaign["campaign_id"],
            "campaign_name": campaign["campaign_name"],
            "customer_id": customer_id,
            "channel": campaign["channel"],
            "message": campaign["message"],
            "sent_date": sent_date,
            "clicked": clicked,
            "purchased": purchased,
        }
    )

campaigns_df = pl.DataFrame(campaign_rows)


positive_reviews = [
    "Easy to use and feels well made.",
    "Good value and I use it often.",
    "Better than I expected overall.",
    "Nice design and works reliably.",
    "Very happy with the purchase.",
]

neutral_reviews = [
    "It does the job, though nothing stood out.",
    "Fine overall with a few small drawbacks.",
    "Useful, but I am not sure I would buy it again.",
    "Pretty average for the price.",
    "Works as expected but could be improved.",
]

negative_reviews = [
    "Did not quite meet my expectations.",
    "The quality felt inconsistent.",
    "I expected more for the price.",
    "Not a great fit for what I needed.",
    "I probably would not purchase this again.",
]

extra_comments = [
    "Shipping was quick.",
    "Packaging was simple.",
    "I bought it after seeing an ad.",
    "A friend recommended it.",
    "The product looked slightly different online.",
    "Delivery took a little longer than expected.",
]

review_rows = []
for i in range(1, N_REVIEWS + 1):
    customer_id = rng.choice(customer_ids)
    customer = customers_by_id[customer_id]
    product = rng.choices(products, weights=product_weights, k=1)[0]
    review_date = random_date()
    rating_score = (
        3.65 + product["quality"] + 0.15 * customer["engagement"] + rng.gauss(0, 0.85)
    )
    rating = round(rating_score)
    rating = max(1, min(5, rating))
    if rating >= 4:
        review_text = rng.choice(positive_reviews)
    elif rating == 3:
        review_text = rng.choice(neutral_reviews)
    else:
        review_text = rng.choice(negative_reviews)
    if rng.random() < 0.20:
        review_text += " " + rng.choice(extra_comments)
    review_rows.append(
        {
            "review_id": f"R{i:06d}",
            "customer_id": customer_id,
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "rating": rating,
            "review_text": review_text,
            "review_date": review_date,
        }
    )
reviews_df = pl.DataFrame(review_rows)


website_rows = []
for i in range(1, N_WEBSITE_VISITS + 1):
    customer_id = rng.choice(customer_ids)
    customer = customers_by_id[customer_id]
    visit_date = random_date()
    source = rng.choices(
        TRAFFIC_SOURCES,
        weights=TRAFFIC_SOURCE_WEIGHTS,
        k=1,
    )[0]
    product = rng.choices(products, weights=product_weights, k=1)[0]
    source_cart_effect = {
        "organic_search": 0.05,
        "paid_search": 0.10,
        "social": -0.05,
        "email": 0.18,
        "direct": 0.08,
        "referral": 0.02,
    }[source]

    cart_score = (
        -1.55
        + 0.55 * customer["engagement"]
        + 0.20 * (product["popularity"] - 1)
        + source_cart_effect
        + 0.30 * (seasonal_multiplier(visit_date) - 1)
        + rng.uniform(-0.20, 0.20)
    )

    added_to_cart = rng.random() < logistic(cart_score)
    source_purchase_effect = {
        "organic_search": 0.02,
        "paid_search": 0.15,
        "social": -0.08,
        "email": 0.14,
        "direct": 0.10,
        "referral": 0.04,
    }[source]
    purchase_score = (
        -2.75
        + 0.45 * customer["engagement"]
        + 1.45 * int(added_to_cart)
        + source_purchase_effect
        + rng.uniform(-0.20, 0.20)
    )
    purchased = rng.random() < logistic(purchase_score)
    website_rows.append(
        {
            "visit_id": f"V{i:06d}",
            "customer_id": customer_id,
            "visit_date": visit_date,
            "traffic_source": source,
            "product_id": product["product_id"],
            "product_viewed": product["product_name"],
            "added_to_cart": added_to_cart,
            "purchased": purchased,
        }
    )

website_df = pl.DataFrame(website_rows)

sales_df.write_csv(OUTPUT_DIR / "sales.csv")
campaigns_df.write_csv(OUTPUT_DIR / "marketing_campaigns.csv")
reviews_df.write_csv(OUTPUT_DIR / "product_reviews.csv")
website_df.write_csv(OUTPUT_DIR / "website_analytics.csv")
