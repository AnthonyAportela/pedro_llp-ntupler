from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "QCD_PT-20to40_Filter_nMuonClusters_gt0_TuneCP5_13p6TeV_pythia8"
config.General.workArea = "crab_projects"
#config.General.transferLogs = True
#config.General.transferOutputs = True

config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "step_combined_QCD20to40.py"
config.JobType.maxMemoryMB = 8000
config.JobType.numCores = 4
config.JobType.outputFiles = ['displacedJetMuon_ntupler.root']

config.Data.outputPrimaryDataset = "QCD_PT-20to40_Filter_nMuonClusters_gt0_TuneCP5_13p6TeV_pythia8"
config.Data.outLFNDirBase = "/store/group/phys_muon/fernanpe/rootfiles/"
config.Data.outputDatasetTag = "QCD_PT-20to40_Run3Summer22"
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False

config.Site.storageSite = "T2_CH_CERN"
