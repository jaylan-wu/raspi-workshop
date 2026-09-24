from rich.console import Console
from rich.table import Table


TEMPERATURES = [
    72.4,
    68.9,
    75.1,
    70.3,
    66.8,
    73.2,
    71.5,
    69.8,
]


def calculate_average(readings):
    """Return the average of all temperature readings."""

    # TODO: Calculate and return the average.
    return 0


def classify_temperature(average):
    """Classify the average temperature."""

    # TODO: Complete the temperature classification.
    return "unknown"


def analyze_temperatures(readings):
    """Analyze a collection of temperature readings."""

    results = {
        "count": len(readings),
        "average": calculate_average(readings),
        "minimum": min(readings),
        "maximum": max(readings),
    }

    results["classification"] = classify_temperature(
        results["average"]
    )

    return results


def display_results(results):
    """Display results in a terminal table."""

    console = Console()
    table = Table(title="Temperature Analysis")

    table.add_column("Measurement")
    table.add_column("Result")

    table.add_row("Number of Readings", str(results["count"]))
    table.add_row("Average", f"{results['average']:.2f} °F")
    table.add_row("Minimum", f"{results['minimum']:.2f} °F")
    table.add_row("Maximum", f"{results['maximum']:.2f} °F")
    table.add_row("Classification", results["classification"])

    console.print(table)


def main():
    results = analyze_temperatures(TEMPERATURES)
    display_results(results)


if __name__ == "__main__":
    main()
