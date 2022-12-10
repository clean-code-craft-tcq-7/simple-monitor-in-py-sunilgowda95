def checkMinExcluded(value, threshold):
    if value < threshold:
        return True
    return False

def checkMaxExcluded(value, threshold):
    if value > threshold:
        return True
    return False
    