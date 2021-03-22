#! /usr/bin/env python
import os

doConvertToPD      = 1 # this already splits into test/train ...
doTrainTestSamples = 0 # this one merges everything
doTraining         = 0
doTestTrainedModel = 0
doPlotValidation   = 0

# massPoints = ['1000','1200','1400','1600','1800','2000']
massPoints = ['1000']
commands = []

inputPath = '/nfs/kloe/einstein4/HDBS/newDataFromRob/'
PDPath = '/nfs/kloe/einstein4/HDBS/DNN_InputDataFrames/'
modelpath = '/nfs/kloe/einstein4/HDBS/DNNModels/test/'

bkgFiles = 'Diboson-0'#,Diboson-1,stop-0,stop-1,ttbar-0,ttbar-1,ttbar-2,ttbar-3,ttbar-4,ttbar-5,Wjets-0,Wjets-1,Wjets-2,Wjets-3,Wjets-4,Wjets-5,Wjets-6,Wjets-8,Wjets-9,Zjets-0,Zjets-1,Zjets-2,Zjets-3,Zjets-4,Zjets-5,Zjets-6,Zjets-7,Zjets-8,Zjets-9,Zjets-10,Zjets-11'
dataFiles = 'Data' # copied from Diboson-1: temporary hack, waiting for actual data files
signalFiles = 'Signal' # IMPORTANT: this one must have exactly this name. Such name is used to assign value 1 to the isSignal flag
# EJS missing: data file, Wjets-7 (missing lep1_m)

mixedFileName = 'MixPD_MergedGGFH'
mode = 'binary'

if doConvertToPD:
    commands += ['python RunML.py --ConvertRootToPD --InputMLNtuplePath '+inputPath+' --inROOTFiles '+bkgFiles+ ',Data,'+signalFiles+' --PreselectionCommand "inPanda[(inPanda.Pass_MergHP_GGF_ZZ_Tag_SR==1) | (inPanda.Pass_MergHP_GGF_ZZ_Untag_SR==1) | (inPanda.Pass_MergLP_GGF_ZZ_Tag_SR==1) | (inPanda.Pass_MergLP_GGF_ZZ_Untag_SR==1) | (inPanda.Pass_MergHP_GGF_ZZ_Tag_ZCR==1) | (inPanda.Pass_MergHP_GGF_ZZ_Untag_ZCR==1) | (inPanda.Pass_MergLP_GGF_ZZ_Tag_ZCR==1) | (inPanda.Pass_MergLP_GGF_ZZ_Untag_ZCR==1)]" --PDPath '+PDPath ]
    # for mass in massPoints:
        # commands += ['python RunML.py -c --inROOTFiles '+signalFiles+mass+' --PreselectionCommand "inPanda[(inPanda.isMerged == 1 )]" ']

if doTrainTestSamples:
    # commands += ['python RunML.py --CreateTrainTestPD --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles ggFH1000  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ ' -m '+mode]
    # commands += ['python RunML.py --CreateTrainTestPD --useEqualSizeSandB --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles ggFH1000  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ '_EqualSB -m '+mode]
    commands += ['python RunML.py --CreateTrainTestPD --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles '+signalFiles+'  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ '_param -m param']
    # EJS: signal files used to be ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000
    # for mass in massPoints:
        # commands += ['python RunML.py -p --inSignalFiles '+signalFiles+mass+'  --inBackgrFiles '+bkgFiles+' --inDataFiles '+dataFiles+'  -N '+mixedFileName+mass+ ' --PreselectionCommand "inPanda[(inPanda.isMerged == 1 ) & (inPanda.isVBFevent == 0)]" ' ]

comboList = [0]
# comboList = range(0,48)

if doTraining:
    for mass in massPoints:
        for combo in comboList:
            # commands += ['python RunML.py --Train --PDPath '+PDPath+' -y '+str(combo)+' --MixPD_TrainTestTag '+mixedFileName+ '  -o DNN_Trained/Train_S1000 -m binary' ]
            commands += ['python RunML.py --Train --PDPath '+PDPath+' -y '+str(combo)+' --MixPD_TrainTestTag '+mixedFileName+ '_param  -o DNN_Trained/Train_param -m param' ]

if doTestTrainedModel:
    # commands += ['python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --PDPath '+PDPath+' --MixPD_TrainTestTag '+mixedFileName+'  --TrainedModelPath DNN_Trained/Train_S1000/'+modelpath+'  -o  DNN_Tests/binary/ -m binary']
    commands += ['python RunML.py --LoadTrainedModel --massPointToTest '"[1000,1200,1400,1600]"' --inSignalFiles=ggFH1000,ggFH1200,ggFH1400 --inDataFiles Data --inBackgrFiles mc16a_Zjets,mc16d_Zjets,mc16e_Zjets,Wjets,Diboson,Top --PDPath '+PDPath+' --MixPD_TrainTestTag '+mixedFileName+'  --TrainedModelPath DNN_Trained/Train_param/'+modelpath+'  -o  DNN_Tests/param/ -m param']


if doPlotValidation:
    for mass in massPoints:
        # commands += ['python RunML.py --ValidPlotsFromTrainTestDF  -N '+mixedFileName+mass]
        commands += ['python RunML.py --ValidPlotsDataMC --inSignalFiles '+signalFiles+mass+' --inBackgrFiles '+bkgFiles+' --inDataFiles '+dataFiles]



for n,i in enumerate(commands):
    print (" ")
    print ("--------------------------------------------")
    print (n,' -- ',i)
    os.system(i)
