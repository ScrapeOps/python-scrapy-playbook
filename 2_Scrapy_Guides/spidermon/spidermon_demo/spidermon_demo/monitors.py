from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.monitors.mixins import StatsMonitorMixin
from spidermon.contrib.actions.slack.notifiers import SendSlackMessageSpiderFinished



#######################################
#####     SPIDEMON MONITORS       #####
#######################################

@monitors.name('Item count')
class ItemCountMonitor(Monitor):

    @monitors.name('Minimum number of items')
    def test_minimum_number_of_items(self):
        item_extracted = getattr(
            self.data.stats, 'item_scraped_count', 0)
        minimum_threshold = 200

        msg = 'Extracted less than {} items'.format(
            minimum_threshold)
        self.assertTrue(
            item_extracted >= minimum_threshold, msg=msg
        )

@monitors.name('Item validation')
class ItemValidationMonitor(Monitor, StatsMonitorMixin):

    @monitors.name('No item validation errors')
    def test_no_item_validation_errors(self):
        validation_errors = getattr(
            self.stats, 'spidermon/validation/fields/errors', 0
        )
        self.assertEqual(
            validation_errors,
            0,
            msg='Found validation errors in {} fields'.format(
                validation_errors)
        )


#######################################
#####   SPIDEMON MONITORSUITES    #####
#######################################

class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        ItemCountMonitor,
        ItemValidationMonitor,
    ]

    monitors_finished_actions = [
        # actions to execute when suite finishes its execution
    ]

    monitors_failed_actions = [
        # actions to execute when suite finishes its execution with a failed monitor
        #SendSlackMessageSpiderFinished, 
    ]



class PeriodicMonitorSuite(MonitorSuite):
    monitors = [
        ItemValidationMonitor,
    ]

    monitors_failed_actions = [
        #SendSlackMessageSpiderFinished, 
    ]


