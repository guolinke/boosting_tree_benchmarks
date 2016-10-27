Speed:
| Data      |  xgboost| xgboost_approx |  LightGBM|
| Higgs|4604.09s |2142.72s |360.766278s |
| Yahoo LTR|704.925s |497.467s |173.392173s |
| MS LTR|1338.28s |1046.48s |263.513085s |


Higgs's AUC:
| Metric      |  xgboost| xgboost_approx |  LightGBM|
| AUC|0.839528|0.840533|0.845123|


NDCG at Yahoo LTR:
| Metric      |  xgboost| xgboost_approx |  LightGBM|
| NDCG@1|0.721213|0.720535|0.731828|
| NDCG@3|0.721025|0.719632|0.738793|
| NDCG@5|0.740316|0.739363|0.756369|
| NDCG@10|0.782226|0.781775|0.796572|


NDCG at MS LTR:
| Metric      |  xgboost| xgboost_approx |  LightGBM|
| NDCG@1|0.488128|0.480611|0.521854|
| NDCG@3|0.472706|0.470275|0.504671|
| NDCG@5|0.476245|0.474441|0.510153|
| NDCG@10|0.495091|0.493346|0.52666|


