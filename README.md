# csv_to_tvalue
csvを読み込みt値を算出する

sample.csv
```csv
405,414
388,410
440,430
397,425
419,434
```

```sh
git clone https://github.com/uehara1414/csv_to_tvalue.git && cd csv_to_tvalue
pip install -r requirements.txt
python t.py sample.csv
>> -1.95790993774
```