import os
import pandas as pd
import glob


def main():
    with open("../data/gakuseki.txt", "r") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]
    lines = map(int, lines)
    cols = ["a_01", "a_02", "a_03", "b_01", "b_02", "b_03", "b_04"]
    df = pd.DataFrame(columns=cols, index=lines)

    for dir_name in df.columns:
        for score in [0, 1, 2]:
            files = glob.glob(f"../data/{dir_name}/score{score}/*")
            for file in files:
                gakuseki = int(os.path.split(file)[1][:8])
                df.loc[gakuseki, dir_name] = score
            # break
    print(df)
    df = df.fillna(0)

    df.to_csv("./score.csv", header=True, index=True)


if __name__ == "__main__":
    main()
