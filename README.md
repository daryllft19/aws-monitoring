# AWS Monitoring
Monitor disk and memory usage for Edukasyon PH's EC2 instances

## Setting up
```
# Create virtual environment to install python modules
# You can put it in $HOME/aws-monitoring/etc
virtualenv -p python3 $HOME/aws-monitoring/etc/venv
source $HOME/aws-monitoring/etc/venv/bin/activate

# Install modules
pip3 install -r $HOME/aws-monitoring/etc/requirements.txt
```

## App Configuration
```
# Modify config $HOME/aws-monitoring/config/.env
# export ENV="<environment_type>-<edukasyon-version>"
export ENV="staging-3.0"
```

## AWS Configuration
```
# Create file $HOME/.aws/config
[default]
region = ap-southeast-1
```

## How to run script
```
source $HOME/aws-monitoring/config/.env && $HOME/aws-monitoring/etc/aws-monitoring-venv/bin/python $HOME/aws-monitoring/disk_mem_usage_cw_metrics.py
```

## Cron Configuration
```
*/1 * * * * source $HOME/aws-monitoring/config/.env && $HOME/aws-monitoring/etc/aws-monitoring-venv/bin/python $HOME/aws-monitoring/disk_mem_usage_cw_metrics.py
```


