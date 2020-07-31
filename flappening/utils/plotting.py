import pandas as pd

import matplotlib.pyplot as plt


def plotHistory(history, config):

    df = pd.DataFrame(history)
    df.to_json(path_or_buf=config["utils"]["output_dir"] + "data.json",
               orient="split")

    # gca stands for 'get current axis'
    ax = plt.gca()

    df.plot(
        kind='line',
        x='epoch',
        y='avg_score',
        ax=ax,
        label='average score',
    )
    df.plot(
        kind='line',
        x='epoch',
        y='best_score',
        color='red',
        ax=ax,
        label='best score',
    )

    plt.legend()
    plt.savefig(config["utils"]["output_dir"] + "plot.png")
