# AWS Monitoring
Monitor ec2 disk and memory usage for edukasyon server's

## App Configuration
```
# Modify config $HOME/aws-monitoring/config/.env
# export ENV="<environment_type>-<edukasyon-version>"
export ENV="staging-3.0"
```

## AWS Configuration
```
# Modify config config/.env
# export ENV="<environment_type>-<edukasyon-version>"
export ENV="staging-3.0"
```

## Cron Configuration
```
*/1 * * * * source $HOME/aws-monitoring/config/.env && $HOME/aws-monitoring/etc/aws-monitoring-venv/bin/python $HOME/aws-monitoring/disk_mem_usage_cw_metrics.py
```


