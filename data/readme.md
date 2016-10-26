## Experiment Data

| Data     |      Task     |  Link | #Train_Set | #Feature| Comments|
|----------|---------------|-------|-------|---------|---------|
| Higgs    |  Binary classification | [link](https://archive.ics.uci.edu/ml/datasets/HIGGS) |10,500,000|28| use last 500,000 samples as test set  | 
| Yahoo LTR|  Learning to rank      | [link](https://webscope.sandbox.yahoo.com/catalog.php?datatype=c)  	|473,134|700|   set1.train as train, set1.test as test |
| MS LTR   |  Learning to rank      | [link](http://research.microsoft.com/en-us/projects/mslr/) |2,270,296|137| {S1,S2,S3} as train set, {S5} as test set |


## How to generate data

1. download above data set
2. move "HIGGS.CSV" in Higgs data set to this folder, and run "higgs2libsvm.py"
3. move "set1.train.txt" and "set1.test.txt" in Yahoo data set to this folder, and run "yahoo2libsvm.py"
4. move "train.txt" and "test.txt" in Fold1 of MSLTR data set to this folder, and run "msltr2libsvm.py"
