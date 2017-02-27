Speed:

| Data      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ----- | ----|
| Higgs|3794.34 s |551.898 s |238.505513 s |
| Yahoo LTR|674.322 s |265.302 s |150.18644 s |
| MS LTR|1251.27 s |385.201 s |215.320316 s |
| Expo|1607.35 s |588.253 s |138.504179 s |
| Allstate|2867.22 s |1355.71 s |348.084475 s |


Higgs's AUC:

| Metric      |  xgboost| xgboost_hist |  LightGBM|
|----|  ----| ---- | ----|
| AUC|0.839593|0.845605|0.845154|


ndcg at Yahoo LTR:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----|
| ndcg@1|0.719748|0.720223|0.732466|
| ndcg@3|0.717813|0.721519|0.738048|
| ndcg@5|0.737849|0.739904|0.756548|
| ndcg@10|0.78089|0.783013|0.796818|


ndcg at MS LTR:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- | -----|
| ndcg@1|0.483956|0.488649|0.524255|
| ndcg@3|0.467951|0.473184|0.505327|
| ndcg@5|0.472476|0.477438|0.510007|
| ndcg@10|0.492429|0.496967|0.527371|


auc at Expo:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- |  ----|
| auc|0.756713|0.777777|0.777543|


auc at Allstate:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- |  ----|
| auc|0.607201|0.609042|0.609167|


