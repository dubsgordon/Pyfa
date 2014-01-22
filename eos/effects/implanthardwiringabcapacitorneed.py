# Used by:
# Implants named like: and Co. Fuel FC (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "capacitorNeed", implant.getModifiedItemAttr("capNeedBonus"))
