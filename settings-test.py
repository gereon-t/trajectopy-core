from trajectopy_core.settings.matching import MatchingMethod


method = "nearest_spatial"

print(MatchingMethod.NEAREST_SPATIAL.value)

test = MatchingMethod(method)

print(test.value)
