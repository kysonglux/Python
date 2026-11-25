from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


COUNTRY = "South Korea"


def plot_life_expectancy(dataset: pd.DataFrame, country: str) -> None:
    """Display life expectancy over time for one country."""
    country_data = dataset[dataset["country"] == country]
    if country_data.empty:
        raise ValueError(f"Country not found: {country}")
    years = [int(column) for column in dataset.columns[1:]]
    values = country_data.iloc[0, 1:].astype(float)
    plt.plot(years, values, label=country)
    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy (years)")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Load the life expectancy dataset and plot the campus country."""
    path = Path(__file__).resolve().parent.parent / "life_expectancy_years.csv"
    dataset = load(str(path))
    if dataset is not None:
        try:
            plot_life_expectancy(dataset, COUNTRY)
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
