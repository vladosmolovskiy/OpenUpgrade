from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "calendar_sms", "15.0.1.1//noupdate_changes.xml")
