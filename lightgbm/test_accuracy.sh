LightGBM/lightgbm config=lightgbm.conf data=../data/higgs.train valid=../data/higgs.test objective=binary metric=auc 2>&1 | tee lightgbm_higgs_accuracy.log

LightGBM/lightgbm config=lightgbm.conf data=../data/msltr.train valid=../data/msltr.test objective=lambdarank metric=ndcg 2>&1 | tee lightgbm_msltr_accuracy.log

LightGBM/lightgbm config=lightgbm.conf data=../data/yahoo.train valid=../data/yahoo.test objective=lambdarank metric=ndcg 2>&1 | tee lightgbm_yahoo_accuracy.log

LightGBM/lightgbm config=lightgbm.conf data=../data/dataexpo_onehot.train valid=../data/dataexpo_onehot.test metric=auc objective=binary 2>&1 | tee lightgbm_dataexpo_accuracy.log

LightGBM/lightgbm config=lightgbm.conf data=../data/allstate.train valid=../data/allstate.test metric=auc objective=binary 2>&1 | tee lightgbm_allstate_accuracy.log






