from django.utils.translation import ugettext as _

from horizon import tabs

from akanda.horizon.firewall.tables import FirewallRuleTable


class FirewallRuleTab(tabs.TableTab):
    name = _("Firewall Rules")
    slug = "firewall_tab"
    table_classes = (FirewallRuleTable,)
    template_name = "horizon/common/_detail_table.html"
    # preload = False

    def get_firewall_rule_data(self):
        from akanda.horizon.fakes import FirewallRuleManager
        return FirewallRuleManager.list_all(self.request)
