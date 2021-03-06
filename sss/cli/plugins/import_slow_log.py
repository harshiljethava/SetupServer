from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook
from sss.core.shellexec import SSSShellExec
from sss.core.logging import Log
from sss.core.variables import SSSVariables
import os


def sss_import_slow_log_hook(app):
    pass


class SSSImportslowlogController(CementBaseController):
    class Meta:
        label = 'import_slow_log'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Import MySQL slow log to Anemometer database'
        usage = "sss import-slow-log"

    @expose(hide=True)
    def default(self):
        Log.info(self, "This command is deprecated."
                 " You can use this command instead, " +
                 Log.ENDC + Log.BOLD + "\n`sss debug --import-slow-log`" +
                 Log.ENDC)


def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(SSSImportslowlogController)

    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', sss_import_slow_log_hook)
