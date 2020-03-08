Speed:

| Data      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ----- | ----|
| Higgs|3794.34 s |165.575 s |130.094667 s |
| Yahoo LTR|674.322 s |131.462 s |76.229267 s |
| MS LTR|1251.27 s |98.3863 s |70.417205 s |
| Expo|1607.35 s |137.65 s |62.607381 s |
| Allstate|2867.22 s |315.256 s |148.231229 s |


Higgs's AUC:

| Metric      |  xgboost| xgboost_hist |  LightGBM|
|----|  ----| ---- | ----|
| AUC|0.839593|0.845314|0.845724|


ndcg at Yahoo LTR:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----|
| ndcg@1|0.719748|0.720049|0.732981|
| ndcg@3|0.717813|0.722573|0.735689|
| ndcg@5|0.737849|0.740899|0.75352|
| ndcg@10|0.78089|0.782957|0.793498|


ndcg at MS LTR:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- | -----|
| ndcg@1|0.483956|0.485115|0.517767|
| ndcg@3|0.467951|0.47313|0.501063|
| ndcg@5|0.472476|0.476375|0.504648|
| ndcg@10|0.492429|0.496553|0.524252|


auc at Expo:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- |  ----|
| auc|0.756713|0.776224|0.776935|


auc at Allstate:

| Metric      |  xgboost | xgboost_hist |  LightGBM|
|----|  ----| ---- |  ----|
| auc|0.607201|0.609465|0.609072|


