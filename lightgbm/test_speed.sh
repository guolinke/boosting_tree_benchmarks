LightGBM/lightgbm config=lightgbm.conf data=../data/higgs.train objective=binary 2>&1 | tee lightgbm_higgs_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/msltr.train objective=lambdarank 2>&1 | tee lightgbm_msltr_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/yahoo.train objective=lambdarank 2>&1 | tee lightgbm_yahoo_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/dataexpo_onehot.train objective=binary  2>&1 | tee lightgbm_dataexpo_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/allstate.train objective=binary num_leaves=127 learning_rate=0.02 2>&1 | tee lightgbm_allstate_speed.log



