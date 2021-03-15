import random,os
from Permutator import *
from ConfigClass import ConfigClass
from HelperTools import *

## All available variables 2-lep
# ['AvgMu','DSID','NBJets','NJets','NLargeRJets','NSigJets','NTrkJets','NTrkJetsinFJ','Nvtx','Pass_LepPt','Pass_MergHP_GGF_WZ_SR','Pass_MergHP_GGF_WZ_TCR','Pass_MergHP_GGF_WZ_ZCR','Pass_MergHP_GGF_ZZ_Tag_SR','Pass_MergHP_GGF_ZZ_Tag_TCR','Pass_MergHP_GGF_ZZ_Tag_ZCR','Pass_MergHP_GGF_ZZ_Untag_SR','Pass_MergHP_GGF_ZZ_Untag_TCR','Pass_MergHP_GGF_ZZ_Untag_ZCR','Pass_MergHP_VBF_WZ_SR','Pass_MergHP_VBF_WZ_TCR','Pass_MergHP_VBF_WZ_ZCR','Pass_MergHP_VBF_ZZ_SR','Pass_MergHP_VBF_ZZ_TCR','Pass_MergHP_VBF_ZZ_ZCR','Pass_MergLP_GGF_WZ_SR','Pass_MergLP_GGF_WZ_TCR','Pass_MergLP_GGF_WZ_ZCR','Pass_MergLP_GGF_ZZ_Tag_SR','Pass_MergLP_GGF_ZZ_Tag_TCR','Pass_MergLP_GGF_ZZ_Tag_ZCR','Pass_MergLP_GGF_ZZ_Untag_SR','Pass_MergLP_GGF_ZZ_Untag_TCR','Pass_MergLP_GGF_ZZ_Untag_ZCR','Pass_MergLP_VBF_WZ_SR','Pass_MergLP_VBF_WZ_TCR','Pass_MergLP_VBF_WZ_ZCR','Pass_MergLP_VBF_ZZ_SR','Pass_MergLP_VBF_ZZ_TCR','Pass_MergLP_VBF_ZZ_ZCR','Pass_Merg_AtLeastOneFatJet','Pass_Merg_GGF_ptVmX','Pass_Merg_VBF_ptVmX','Pass_Merg_bVeto','Pass_Merg_isWZJet','Pass_Merg_isWZJetLP','Pass_Mll','Pass_MuonEtaLt2p5','Pass_OSMuons','Pass_Res_Found_had_W','Pass_Res_Found_had_Z','Pass_Res_GGF_WZ_SR','Pass_Res_GGF_WZ_TCR','Pass_Res_GGF_WZ_ZCR','Pass_Res_GGF_ZZ_Tag_SR','Pass_Res_GGF_ZZ_Tag_TCR','Pass_Res_GGF_ZZ_Tag_ZCR','Pass_Res_GGF_ZZ_Untag_SR','Pass_Res_GGF_ZZ_Untag_TCR','Pass_Res_GGF_ZZ_Untag_ZCR','Pass_Res_GGF_ptVmX_W','Pass_Res_GGF_ptVmX_Z','Pass_Res_LeadJet60_W','Pass_Res_LeadJet60_Z','Pass_Res_MassWindow_W','Pass_Res_MassWindow_Z','Pass_Res_SubleadJet45_W','Pass_Res_SubleadJet45_Z','Pass_Res_VBF_WZ_SR','Pass_Res_VBF_WZ_TCR','Pass_Res_VBF_WZ_ZCR','Pass_Res_VBF_ZZ_SR','Pass_Res_VBF_ZZ_TCR','Pass_Res_VBF_ZZ_ZCR','Pass_Res_VBF_ptVmX_W','Pass_Res_VBF_ptVmX_Z','Pass_Res_bVetoTag_Z','Pass_Res_bVetoUntag_W','Pass_Res_bVetoUntag_Z','Pass_SFLeptons','Pass_SigJetORFatJet','Pass_Trigger','Pass_WTagger','Pass_WTaggerMassCut','Pass_WTaggerMassCutLP','Pass_WTaggerSubStructCut','Pass_WTaggerSubStructCutLP','Pass_ZTagger','Pass_ZTaggerMassCut','Pass_ZTaggerMassCutLP','Pass_ZTaggerSubStructCut','Pass_ZTaggerSubStructCutLP','Pass_isVBF','RNNScore_VW','RNNScore_VZ','Wdijet_eta','Wdijet_m','Wdijet_phi','Wdijet_pt','X_boosted_eta','X_boosted_m','X_boosted_phi','X_boosted_pt','X_resolved_WW_eta','X_resolved_WW_m','X_resolved_WW_phi','X_resolved_WW_pt','X_resolved_WZ_eta','X_resolved_WZ_m','X_resolved_WZ_phi','X_resolved_WZ_pt','ZPV','Zcand_eta','Zcand_m','Zcand_phi','Zcand_pt','Zdijet_eta','Zdijet_m','Zdijet_phi','Zdijet_pt','bTagSF','eventNumber','fatjet_D2','fatjet_eta','fatjet_m','fatjet_nAddBTags','fatjet_nBTags','fatjet_phi','fatjet_pt','isLep1MuonFlavour','isLep2MuonFlavour','lep1_eta','lep1_m','lep1_phi','lep1_pt','lep2_eta','lep2_m','lep2_phi','lep2_pt','mu','sigWJ1_MV2c10','sigWJ1_e','sigWJ1_eta','sigWJ1_isTag','sigWJ1_m','sigWJ1_phi','sigWJ1_pt','sigWJ2_MV2c10','sigWJ2_e','sigWJ2_eta','sigWJ2_isTag','sigWJ2_m','sigWJ2_phi','sigWJ2_pt','sigZJ1_MV2c10','sigZJ1_e','sigZJ1_eta','sigZJ1_isTag','sigZJ1_m','sigZJ1_phi','sigZJ1_pt','sigZJ2_MV2c10','sigZJ2_e','sigZJ2_eta','sigZJ2_isTag','sigZJ2_m','sigZJ2_phi','sigZJ2_pt','tagJ1_e','tagJ1_eta','tagJ1_m','tagJ1_phi','tagJ1_pt','tagJ2_e','tagJ2_eta','tagJ2_m','tagJ2_phi','tagJ2_pt','tagJJ_deta','tagJJ_m','trkJetBTagSF','trkjet1_MV2c10','trkjet1_R','trkjet1_eta','trkjet1_isTag','trkjet1_m','trkjet1_nTrk','trkjet1_phi','trkjet1_pt','trkjet2_MV2c10','trkjet2_R','trkjet2_eta','trkjet2_isTag','trkjet2_m','trkjet2_nTrk','trkjet2_phi','trkjet2_pt','trkjets_DR','wBosonTagSF','weight','zBosonTagSF']

rootBranchSubSample= ['lep1_m', 'lep1_pt', 'lep1_eta', 'lep1_phi', 'lep2_m','lep2_pt', 'lep2_eta', 'lep2_phi', 'fatjet_m', 'fatjet_pt', 'fatjet_eta', 'fatjet_phi', 'fatjet_D2', 'NJets', 'weight', 'X_boosted_m', 'Pass_MergHP_GGF_ZZ_Tag_SR', 'Pass_MergHP_GGF_ZZ_Untag_SR', 'Pass_MergLP_GGF_ZZ_Tag_SR', 'Pass_MergLP_GGF_ZZ_Untag_SR', 'Pass_MergHP_GGF_ZZ_Tag_ZCR', 'Pass_MergHP_GGF_ZZ_Untag_ZCR', 'Pass_MergLP_GGF_ZZ_Tag_ZCR', 'Pass_MergLP_GGF_ZZ_Untag_ZCR']
# EJS missing: isSignal, truth_zv_mass, isMerged, isCR, isVBFEvent, ll_m, ll_pt, lep1_e turned to lep1_m, same for lep2 and fatjet

VariablesToPlot = [
    # 'lep1_pt','lep1_eta','lep2_pt','lep2_eta','Zll_mass','fatjet_pt','Zll_pt','truth_zv_mass'
]

InputDNNVariables = [
        # MERGED - DNN
       # ['lep1_m', 'lep1_pt', 'lep1_eta', 'lep1_phi', 'lep2_m','lep2_pt', 'lep2_eta', 'lep2_phi', 'll_m', 'll_pt','fatjet_m', 'fatjet_pt', 'fatjet_eta', 'fatjet_phi','NJets'],

       # MERGED - pDNN
       ['lep1_m', 'lep1_pt', 'lep1_eta', 'lep1_phi', 'lep2_m','lep2_pt', 'lep2_eta', 'lep2_phi', 'll_m', 'll_pt', 'fatjet_m', 'fatjet_pt', 'fatjet_eta', 'fatjet_phi', 'NJets','truth_zv_mass'],

       # RESOLVED - pDNN
       # ['lep1_m', 'lep1_pt', 'lep1_eta', 'lep1_phi', 'lep2_m','lep2_pt', 'lep2_eta', 'lep2_phi', 'll_m', 'll_pt', 'jj_pt', 'jj_j1pt', 'jj_eta', 'jj_phi','jj_m', 'jj_j1eta', 'jj_j1phi', 'jj_j1M', 'jj_j1NTracks', 'jj_j2pt', 'jj_j2eta', 'jj_j2phi', 'jj_j2M', 'jj_j2NTracks', 'NJETS','truth_zv_mass'],

        ]

ScanParams = {
    "Width":[64,128,2000]
    ,"BatchSize": [1024,2048]
    ,"Depth":[3,4,5]
    ,"LearningRate": [0.0003, 0.003]
    ,"VarSet": [ i for i in range(0,len(InputDNNVariables))]

}

#FixedParams
Params = {
    "WeightInitialization": "'normal'",
    "Epochs": 200,
    "Optimizer": "Adam"
}

# Apply dropout when building the NN(see ModelBuilder.py)
Dropout       = 0.2 #0.2-->20% of the nodes will be ommitted. Put a negative value if you want to switch off the dropout


def getScanParamCombos(setupClient):
    PS=Permutator(setupClient.ScanParams)
    Combos=PS.Permutations()
    return Combos

def printScanParamCombos(setupClient):
    Combos = getScanParamCombos(setupClient)
    print ("Parameter Scan: ", len(Combos), "possible combinations.")
    for j in range(0,len(Combos)):
        print (j,":",Combos[j])

def pickModelParamSet(setupClient):
    i=-1
    Combos = getScanParamCombos(setupClient)
    if setupClient.HyperParamSet >=0:
        i=int(setupClient.HyperParamSet)

    if i<0:
        random.seed()
        i=int(round(len(Combos)*random.random()))

    print ('{:<45} {:<15}'.format('Picked combination',Fore.GREEN + str(i) + (' Manualy' if setupClient.HyperParamSet >=0 else ' Randomly')) )
    if i==len(Combos):
        i=i-1

    for k in Combos[i]:
        setupClient.Params[k]=Combos[i][k]


    ModelName=setupClient.modelPrefixName

    for param in ScanParams.keys():
        val=str(setupClient.Params[param]).replace('"',"")
        if param=='VarSet':
            ModelName+="_VarSet"+val.replace("'","")
        else:
            ModelName+="_"+val.replace("'","")

    setupClient.ModelParamCombo = ModelName
    print ('{:<45} {:<15}'.format('Model Name',Fore.GREEN+ModelName))
    ModelSavePath = os.path.join(setupClient.OutBaseDir, ModelName)
    # ModelSavePath will point to OutBaseDir+ModelName
    setupClient.ModelSavePath = ModelSavePath
    print ('{:<45} {:<15}'.format('ModelOuput directory',Fore.GREEN + setupClient.ModelSavePath ), checkCreateDir(setupClient.ModelSavePath) )

    setupClient.HyperParamSet = i
    setupClient.VarSet = setupClient.Params['VarSet']
