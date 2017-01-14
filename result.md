Speed:

| Data      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| Higgs|4604.09 s |2142.72 s |727.914 s |310.648077 s |
| Yahoo LTR|704.925 s |497.467 s |444.428 s |175.559103 s |
| MS LTR|1338.28 s |1046.48 s |492.003 s |260.482291 s |
| Expo|1897.94 s |800.425 s |n/a |116.587805 s |


Higgs's AUC:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| AUC|0.839528|0.840533|0.845617|0.845123|


ndcg at Yahoo LTR:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| ndcg@1|0.721213|0.720535|0.719658|0.735666|
| ndcg@3|0.721025|0.719632|0.71993|0.73712|
| ndcg@5|0.740316|0.739363|0.738821|0.755813|
| ndcg@10|0.782226|0.781775|0.781864|0.796394|


ndcg at MS LTR:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| ndcg@1|0.488128|0.480611|0.485735|0.524291|
| ndcg@3|0.472706|0.470275|0.469604|0.50432|
| ndcg@5|0.476245|0.474441|0.475067|0.509229|
| ndcg@10|0.495091|0.493346|0.494194|0.526746|


auc at Expo:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| auc|0.75548|0.757071|n/a|0.781061|


