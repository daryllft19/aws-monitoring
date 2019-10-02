# AWS Monitoring
A simple plugin that monitors disk and memory usage for Edukasyon PH's EC2 instances then sends metrics to cloudwatch.

## Setting up
```
# Create virtual environment to install python modules
# You can put it in $HOME/aws-monitoring/etc

virtualenv -p python3 $HOME/aws-monitoring/etc/aws-monitoring-venv
source $HOME/aws-monitoring/etc/aws-monitoring-venv/bin/activate


# Install modules

pip3 install -r $HOME/aws-monitoring/etc/requirements.txt
```

## App Configuration
```
# Modify config $HOME/aws-monitoring/config/.env
# export ENV="<environment_type>-<edukasyon-version>-<type>"
# This is entirely up to us but preferrably with convention since this can serve as a filter in cloudwatch

export ENV="staging-3.0-edos"
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

#### For some reason, cron in ubuntu needed a separate runner to contain the file as opposed to ami linux that we could just put the code straight

```
# After ensuring that the script works, we can setup the cron config

*/1 * * * * source $HOME/aws-monitoring/config/.env && $HOME/aws-monitoring/etc/aws-monitoring-venv/bin/python $HOME/aws-monitoring/disk_mem_usage_cw_metrics.py
```


