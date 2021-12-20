BOT_NAME = 'spidermon_demo'

SPIDER_MODULES = ['spidermon_demo.spiders']
NEWSPIDER_MODULE = 'spidermon_demo.spiders'
LOG_LEVEL = 'INFO'

#######################################
#####    SPIDEMON INTEGRATION     #####
#######################################

SPIDERMON_ENABLED = True

EXTENSIONS = {
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}


ITEM_PIPELINES = {
    'spidermon.contrib.scrapy.pipelines.ItemValidationPipeline': 800,
}

## Active Item Validators
SPIDERMON_VALIDATION_MODELS = (
    'spidermon_demo.validators.BookItem',
)


## Active Monitor Suites
SPIDERMON_SPIDER_OPEN_MONITORS = (
    # list of monitor suites to be executed when the spider starts
)

SPIDERMON_SPIDER_CLOSE_MONITORS = (
    'spidermon_demo.monitors.SpiderCloseMonitorSuite',
)


SPIDERMON_PERIODIC_MONITORS = {
    'spidermon_demo.monitors.PeriodicMonitorSuite': 5,  # time in seconds
}


## Slack Notifications
SPIDERMON_SLACK_SENDER_TOKEN = '<SLACK_SENDER_TOKEN>'
SPIDERMON_SLACK_SENDER_NAME = '<SLACK_SENDER_NAME>'
SPIDERMON_SLACK_RECIPIENTS = ['@yourself', '#yourprojectchannel']


