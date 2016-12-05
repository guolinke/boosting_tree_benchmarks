LightGBM/lightgbm config=lightgbm.conf data=../data/higgs.train objective=binary 2>&1 | tee lightgbm_higgs_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/msltr.train objective=lambdarank 2>&1 | tee lightgbm_msltr_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/yahoo.train objective=lambdarank 2>&1 | tee lightgbm_yahoo_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/dataexpo_onehot.train objective=binary  2>&1 | tee lightgbm_dataexpo_onehot_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/dataexpo.train categorical_column=0,1,2,4,5,6 objective=binary 2>&1 | tee lightgbm_dataexpo_speed.log




