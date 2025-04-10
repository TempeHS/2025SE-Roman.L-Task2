def validate(features):
    if len(features[0]) != 6:
        return False
    for feature in features[0]:
        if not isinstance(feature, (int, float)):
            return False
    return True
