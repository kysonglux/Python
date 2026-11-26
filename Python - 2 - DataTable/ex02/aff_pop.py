from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

from load_csv import load


COUNTRY = "Luxembourg"
COMPARISON_COUNTRY = "France"


def plot_population(
    dataset: pd.DataFrame,
    country: str,
    comparison_country: str,
) -> None:
    """Display population over 1800-2050 for two countries."""
    country_data = dataset[dataset["country"].isin(
        [country, comparison_country]
    )]
    if len(country_data) != 2:
        raise ValueError("One or more countries were not found")
    years = [int(column) for column in dataset.columns[1:]]
    for _, row in country_data.iterrows():
        values = row.iloc[1:].map(_parse_value)
        plt.plot(years, values, label=row["country"])
    plt.title(f"Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda value, _: f"{value / 1_000_000:g}M")
    )
    plt.xlim(1800, 2050)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()
    plt.savefig("test.png")


def _parse_value(value: str) -> float:
    """Convert Gapminder's abbreviated number format to a float."""
    text = str(value).strip()
    suffixes = {"k": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    if text and text[-1] in suffixes:
        return float(text[:-1]) * suffixes[text[-1]]
    return float(text)


def main() -> None:
    """Load the population dataset and plot two countries."""
    path = Path(__file__).resolve().parent.parent / "population_total.csv"
    dataset = load(str(path))
    if dataset is not None:
        try:
            plot_population(dataset, COUNTRY, COMPARISON_COUNTRY)
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
