def GetTimeFromLightGBM(filename):
	input = open(filename, "r")
	ret = 0.0
	for line in input.readlines():
		if 'seconds elapsed, finished' in line:
			ret = float(line.split('seconds')[0].strip().split(' ')[-1])
	return ret
def GetAccuracyFromLightGBM(filename, key):
	input = open(filename, "r")
	ret = 0.0
	for line in input.readlines():
		if key + ' :' in line:
			ret = max(ret,float(line.split(key+' :')[-1]))
	return ret
def GetTimeFromXgboost(filename):
	input = open(filename, "r")
	ret = 0.0
	for line in input.readlines():
		if 'boosting round' in line and 'sec elapsed' in line:
			ret = float(line.split(',')[1].strip().split(' ')[0])
	return ret
def GetAccuracyFromXgboost(filename, key):
	input = open(filename, "r")
	ret = 0.0
	for line in input.readlines():
		if 'test-' in line and key in line:
			ret = max(ret,float(line.split(key+':')[1].split('\t')[0]))
	return ret

lightgbm_speed_result = [GetTimeFromLightGBM('lightgbm/lightgbm_higgs_speed.log')
	,GetTimeFromLightGBM('lightgbm/lightgbm_yahoo_speed.log')
	,GetTimeFromLightGBM('lightgbm/lightgbm_msltr_speed.log')
	,GetTimeFromLightGBM('lightgbm/lightgbm_dataexpo_speed.log')]

lightgbm_higgs_accuracy = [GetAccuracyFromLightGBM('lightgbm/lightgbm_higgs_accuracy.log', "auc")]

lightgbm_yahoo_accuracy = [GetAccuracyFromLightGBM('lightgbm/lightgbm_yahoo_accuracy.log', "ndcg@1")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_yahoo_accuracy.log', "ndcg@3")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_yahoo_accuracy.log', "ndcg@5")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_yahoo_accuracy.log', "ndcg@10")]

lightgbm_msltr_accuracy = [GetAccuracyFromLightGBM('lightgbm/lightgbm_msltr_accuracy.log', "ndcg@1")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_msltr_accuracy.log', "ndcg@3")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_msltr_accuracy.log', "ndcg@5")
,GetAccuracyFromLightGBM('lightgbm/lightgbm_msltr_accuracy.log', "ndcg@10")]

lightgbm_expo_one_hot_accuracy = [GetAccuracyFromLightGBM('lightgbm/lightgbm_dataexpo_onehot_accuracy.log', "auc") ]

lightgbm_expo_accuracy = [GetAccuracyFromLightGBM('lightgbm/lightgbm_dataexpo_accuracy.log', "auc") ]

xgboost_speed_result = [GetTimeFromXgboost('xgboost/xgboost_higgs_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_yahoo_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_msltr_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_dataexpo_onehot_speed.log')]

xgboost_higgs_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_higgs_accuracy.log', "auc")]

xgboost_yahoo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_yahoo_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_yahoo_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_yahoo_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_yahoo_accuracy.log', "ndcg@10")]

xgboost_msltr_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_msltr_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_msltr_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_msltr_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_msltr_accuracy.log', "ndcg@10")]

xgboost_expo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_dataexpo_onehot_accuracy.log', "auc")]

xgboost_approx_speed_result = [GetTimeFromXgboost('xgboost/xgboost_approx_higgs_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_approx_yahoo_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_approx_msltr_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_approx_dataexpo_onehot_speed.log')]

xgboost_approx_higgs_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_approx_higgs_accuracy.log', "auc")]

xgboost_approx_yahoo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_approx_yahoo_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_yahoo_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_yahoo_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_yahoo_accuracy.log', "ndcg@10")]

xgboost_approx_msltr_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_approx_msltr_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_msltr_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_msltr_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_approx_msltr_accuracy.log', "ndcg@10")]

xgboost_hist_speed_result = [GetTimeFromXgboost('xgboost/xgboost_hist_higgs_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_hist_yahoo_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_hist_msltr_speed.log')
	,GetTimeFromXgboost('xgboost/xgboost_hist_dataexpo_onehot_speed.log')]

xgboost_hist_higgs_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_hist_higgs_accuracy.log', "auc")]

xgboost_hist_yahoo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_hist_yahoo_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_yahoo_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_yahoo_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_yahoo_accuracy.log', "ndcg@10")]

xgboost_hist_msltr_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_hist_msltr_accuracy.log', "ndcg@1")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_msltr_accuracy.log', "ndcg@3")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_msltr_accuracy.log', "ndcg@5")
,GetAccuracyFromXgboost('xgboost/xgboost_hist_msltr_accuracy.log', "ndcg@10")]


xgboost_hist_expo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_hist_dataexpo_onehot_accuracy.log', "auc")]

xgboost_approx_expo_accuracy = [GetAccuracyFromXgboost('xgboost/xgboost_approx_dataexpo_onehot_accuracy.log', "auc")]
output = open("result.md", "w")
output.write("Speed:\n\n")
Title = ["Higgs", "Yahoo LTR", "MS LTR", "Expo"]
speed_result = [xgboost_speed_result, xgboost_approx_speed_result, xgboost_hist_speed_result, lightgbm_speed_result]
output.write('| Data      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|\n')
output.write('|----|  ----| ---- | ----- | ----|\n')
for i in range(len(Title)):
	output.write('| ' + Title[i] + '|')
	for j in range(len(speed_result)):
		output.write(str(speed_result[j][i]) + ' s |')
	output.write('\n')

output.write('\n\n')

output.write("Higgs's AUC:\n\n")
Title = ["AUC"]
speed_result = [xgboost_higgs_accuracy, xgboost_approx_higgs_accuracy, xgboost_hist_higgs_accuracy, lightgbm_higgs_accuracy]
output.write('| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|\n')
output.write('|----|  ----| ---- | ----- | ----|\n')
for i in range(len(Title)):
	output.write('| ' + Title[i] + '|')
	for j in range(len(speed_result)):
		output.write(str(speed_result[j][i]) + '|')
	output.write('\n')

output.write('\n\n')

output.write("ndcg at Yahoo LTR:\n\n")
Title = ["ndcg@1","ndcg@3","ndcg@5","ndcg@10"]
speed_result = [xgboost_yahoo_accuracy, xgboost_approx_yahoo_accuracy, xgboost_hist_yahoo_accuracy, lightgbm_yahoo_accuracy]
output.write('| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|\n')
output.write('|----|  ----| ---- | ----- | ----|\n')
for i in range(len(Title)):
	output.write('| ' + Title[i] + '|')
	for j in range(len(speed_result)):
		output.write(str(speed_result[j][i]) + '|')
	output.write('\n')

output.write('\n\n')


output.write("ndcg at MS LTR:\n\n")
Title = ["ndcg@1","ndcg@3","ndcg@5","ndcg@10"]
speed_result = [xgboost_msltr_accuracy, xgboost_approx_msltr_accuracy, xgboost_hist_msltr_accuracy, lightgbm_msltr_accuracy]
output.write('| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|\n')
output.write('|----|  ----| ---- | ----- | ----|\n')
for i in range(len(Title)):
	output.write('| ' + Title[i] + '|')
	for j in range(len(speed_result)):
		output.write(str(speed_result[j][i]) + '|')
	output.write('\n')

output.write('\n\n')

output.write("auc at Expo:\n\n")
Title = ["auc"]
speed_result = [xgboost_expo_accuracy, xgboost_approx_expo_accuracy, xgboost_hist_expo_accuracy ,lightgbm_expo_accuracy]
output.write('| Metric      |  xgboost| xgboost_approx | xgboost_hist |  LightGBM|\n')
output.write('|----|  ----| ---- | ----- | ----|\n')
for i in range(len(Title)):
	output.write('| ' + Title[i] + '|')
	for j in range(len(speed_result)):
		output.write(str(speed_result[j][i]) + '|')
	output.write('\n')

output.write('\n\n')


output.close()



