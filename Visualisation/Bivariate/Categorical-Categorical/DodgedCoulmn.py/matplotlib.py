import matplotlib.pyplot as plt
import numpy as np


def dodged_column_plot(
    categories,
    subcategories,
    values,
    colors=None,
    width=0.8,
    figsize=(8, 5),
    title=None,
    xlabel=None,
    ylabel=None,
    legend_title=None,
    annotate=False,
    annotation_fmt="{}",
    annotation_color="black",
):
    """Create a dodged column plot in matplotlib.

    categories: list of category labels for the x-axis.
    subcategories: list of subgroup labels for each series.
    values: list of lists or 2D array with shape (len(subcategories), len(categories)).
    """
    categories = list(categories)
    subcategories = list(subcategories)
    values = np.asarray(values)

    if values.ndim != 2 or values.shape[0] != len(subcategories) or values.shape[1] != len(categories):
        raise ValueError(
            "values must be a 2D array with shape (len(subcategories), len(categories))"
        )

    n_groups = len(categories)
    n_sub = len(subcategories)
    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    if len(colors) < n_sub:
        colors = list(colors) * ((n_sub + len(colors) - 1) // len(colors))

    x = np.arange(n_groups)
    bar_width = width / n_sub

    fig, ax = plt.subplots(figsize=figsize)

    for idx, (subcat, subvals) in enumerate(zip(subcategories, values)):
        offset = (idx - (n_sub - 1) / 2) * bar_width
        ax.bar(
            x + offset,
            subvals,
            bar_width,
            label=subcat,
            color=colors[idx],
            edgecolor="black",
        )
        if annotate:
            for xpos, height in zip(x + offset, subvals):
                ax.text(
                    xpos,
                    height,
                    annotation_fmt.format(height),
                    ha="center",
                    va="bottom",
                    color=annotation_color,
                    fontsize=9,
                )

    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if legend_title:
        ax.legend(title=legend_title)
    else:
        ax.legend()

    ax.set_ylim(0, np.max(values) * 1.1)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return fig, ax


if __name__ == "__main__":
    categories = ["A", "B", "C", "D"]
    subcategories = ["Group 1", "Group 2", "Group 3"]
    values = [[5, 7, 6, 8], [4, 6, 5, 7], [3, 5, 4, 6]]

    fig, ax = dodged_column_plot(
        categories,
        subcategories,
        values,
        title="Dodged Column Plot",
        xlabel="Category",
        ylabel="Value",
        legend_title="Groups",
        annotate=True,
    )
    plt.show()
