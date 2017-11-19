labels=("butterfly" "bee" "beetle")
length=${#labels[@]}

for (( i=0; i<${length}; i++ ));
do
    for(( j=1; j<=15; j++));
    do
        item="$j"
        if [ $j -lt 10 ]
        then
            item="0$j"
        fi
        # echo "${labels[$i]} $item"
        python dic_batch_process.py ${labels[$i]} $item
    done
done

mkdir test_summary
mv *.csv test_summary/
