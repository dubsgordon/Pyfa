# Used by:
# Celestials named like: Pulsar Effect Beacon Class (6 of 6)
# Celestials named like: Wolf Rayet Beacon (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("signatureRadius", beacon.getModifiedItemAttr("signatureRadiusMultiplier"))
