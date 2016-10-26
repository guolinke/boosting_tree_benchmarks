LightGBM/lightgbm config=lightgbm.conf data=../data/higgs.train valid=../data/higgs.test objective=binary metric=auc 2>&1 | tee lightgbm_higgs.log
LightGBM/lightgbm config=lightgbm.conf data=../data/higgs.train objective=binary 2>&1 | tee lightgbm_higgs_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/msltr.train valid=../data/msltr.test objective=lambdarank metric=ndcg 2>&1 | tee lightgbm_msltr.log
LightGBM/lightgbm config=lightgbm.conf data=../data/msltr.train objective=lambdarank 2>&1 | tee lightgbm_msltr_speed.log

LightGBM/lightgbm config=lightgbm.conf data=../data/yahoo.train valid=../data/yahoo.test objective=lambdarank metric=ndcg 2>&1 | tee lightgbm_yahoo.log
LightGBM/lightgbm config=lightgbm.conf data=../data/yahoo.train objective=lambdarank 2>&1 | tee lightgbm_yahoo_speed.log





