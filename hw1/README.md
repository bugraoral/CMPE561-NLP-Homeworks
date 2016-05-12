#How To Run

```
$cd hw1
$python3.5 main.py
```

More options are
```
 -t or --training Training set Path
 -v or --validation Test set Path
 -r or --path Raw dataset path
 -d or --dirty Re-split and tokenize if set to true than the pregenerated split and token paths will be used if they exist
 -vb or --verbose verbose loggining predictions
```

```
$python3.5 main.py -r path_to_raw_data
```
```
$python3.5 main.py -t path_to_training_set
```
```
$python3.5 main.py -t path_to_raw_data -v path_to_validation_set
```

To add extra predefined features:
Number of words:

```
$python3.5 main.py --nwords
```

Number of commas:

```
$python3.5 main.py --ncommas
```

To run with pre-splited data
```
$python3.5 main.py -d
```
To see more information
```
$python3.5 main.py -vb
```
