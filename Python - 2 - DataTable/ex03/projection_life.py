from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

from load_csv import load


YEAR = "1900"


def _parse_value(value: str) -> float:
    """Convert Gapminder's abbreviated number format to a float."""
    text = str(value).strip()
    suffixes = {"k": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    if text and text[-1] in suffixes:
        return float(text[:-1]) * suffixes[text[-1]]
    return float(text)


def plot_projection(income: pd.DataFrame, life: pd.DataFrame) -> None:
    """Display life expectancy against income for a selected year."""
    if YEAR not in income.columns or YEAR not in life.columns:
        raise ValueError(f"Year not found: {YEAR}")
    income_year = income[["country", YEAR]].copy()
    life_year = life[["country", YEAR]].copy()
    merged = income_year.merge(life_year, on="country", suffixes=("_income", "_life"))
    merged["income"] = merged[f"{YEAR}_income"].map(_parse_value)
    merged["life_expectancy"] = merged[f"{YEAR}_life"].astype(float)
    merged = merged.dropna(subset=["income", "life_expectancy"])
    plt.scatter(merged["income"], merged["life_expectancy"], alpha=0.7)
    plt.xscale("log")
    plt.gca().xaxis.set_major_formatter(
        FuncFormatter(lambda value, _: f"{value / 1_000:g}k")
    )
    plt.title(f"{YEAR}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.tight_layout()
    plt.show()
    plt.savefig(Path(__file__).resolve().parent / "test.png")


def main() -> None:
    """Load both datasets and display their projection for 1900."""
    base = Path(__file__).resolve().parent
    income = load(str(base / "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
    life = load(str(base / "life_expectancy_years.csv"))
    if income is not None and life is not None:
        try:
            plot_projection(income, life)
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
