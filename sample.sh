#!/bin/bash

data_dir="./data/b_04"
mkdir -p $data_dir/score0
mkdir -p $data_dir/score1
mkdir -p $data_dir/score2

for file in `ls ${data_dir}/*.c`; do
    echo $file
    gcc ${file}

    # コンパイルエラー
    if [ $? -ne 0 ]; then
        echo $file
        mv $file $data_dir/score0/
        continue
    fi

    ./a.exe < $data_dir/answer/input.txt
    # ./a.exe
    echo -n "YES:j or NO:p":
    read judge

    if [ "$judge" = "j" ]; then
        echo "OK"
        code $file
        echo -n "---FINAL JUDGE(j or score1 or score0)---:"
        read final_judge
        if [ "$final_judge" = "j" ]; then
            echo "All OK"
            mv $file $data_dir/score2/
        elif [ "$final_judge" = "score1" ]; then
            echo "score1"
            mv $file $data_dir/score1/
        elif [ "$final_judge" = "score0" ]; then
            echo "score0"
            mv $file $data_dir/score0/
        else
            echo "Other"
        fi
    elif [ "$judge" = "p" ]; then
        echo "NG"
        mv $file $data_dir/score0/
    elif [ "$judge" = "q" ]; then
        echo "exit"
        exit 0
    else
        echo "Other"
    fi
    # break
done
