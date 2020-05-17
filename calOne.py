import logicTestV2
import logisticV2
import sys

code = sys.argv[1]
date = sys.argv[2]

logisticV2.GeneratingParameters(date, code)
logicTestV2.forecast(code, date)
