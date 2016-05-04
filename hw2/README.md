#Training
To train the model use train_hmm_tagger.py like follows

```
python3.5 train_hmm_tagger.py metu_sabanci_cmpe_561_v2/train/turkish_metu_sabanci_train.conll --postag
```
or
```
python3.5 train_hmm_tagger.py metu_sabanci_cmpe_561_v2/train/turkish_metu_sabanci_train.conll --cpostag
```

#Validation
The trained model can be used for tagging any conll file.
Here is an example
```
hmm_tagger.py metu_sabanci_cmpe_561_v2/validation/turkish_metu_sabanci_val.conll validation_results.txt
```

#Evaluation
The output of the hmm_tagger.py can evaluated using evaluate_hmm_tagger.py
Here is how you would evaluate the previously generated validation output file.

```
python3.5 evaluate_hmm_tagger.py validation_results.txt metu_sabanci_cmpe_561_v2/validation/turkish_metu_sabanci_val.conll --postag
```

This will print out the results and create a .csv file containing a confusion matrix.
