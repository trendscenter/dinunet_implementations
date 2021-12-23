from coinstac_dinunet.site_runner import SiteRunner

from comps.icalstm import ICATrainer, ICADataHandle, ICADataset

if __name__ == "__main__":
    runner = SiteRunner(taks_id='FSL', data_path='../../datasets/icalstm', mode='Train',
                        split_ratio=[0.8, 0.1, 0.1], monitor_metric='auc', log_header='Loss|Auc')
    runner.run(ICATrainer, ICADataset, ICADataHandle)
