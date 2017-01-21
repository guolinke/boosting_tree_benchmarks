Speed:

| Data      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| Higgs|3856.06 s |2256.88 s |582.192 s |262.364174 s |
| Yahoo LTR|671.803 s |479.533 s |265.916 s |167.210277 s |
| MS LTR|1257.1 s |1078.87 s |384.832 s |255.209744 s |
| Expo|1609.92 s |788.811 s |619.339 s |106.620605 s |


Higgs's AUC:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| AUC|0.839593|0.840521|0.845605|0.84611|


ndcg at Yahoo LTR:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| ndcg@1|0.719748|0.717839|0.720223|0.731098|
| ndcg@3|0.717813|0.718188|0.721519|0.736522|
| ndcg@5|0.737849|0.738389|0.739904|0.754748|
| ndcg@10|0.78089|0.780146|0.783013|0.796101|


ndcg at MS LTR:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| ndcg@1|0.483956|0.487025|0.488649|0.524228|
| ndcg@3|0.467951|0.468897|0.473184|0.50649|
| ndcg@5|0.472476|0.473395|0.477438|0.510901|
| ndcg@10|0.492429|0.49303|0.496967|0.527279|


auc at Expo:

| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|
|----|  ----| ---- | ----- | ----|
| auc|0.756713|0.755311|0.777777|0.774906|


