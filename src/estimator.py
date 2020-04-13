# convert period type
def nomilise(timeToElapse, periodType):
    period = 1
    if periodType == "days":
        period = timeToElapse
    elif periodType == "weeks":
        period = int((timeToElapse * 7) / 3)
    elif periodType == "months":
        period = int(timeToElapse * 30)
    return int(period)

def estimator(data):

    impact = solve(data, 10)
    severeImpact = solve(data, 50)

    return {"data": data, "impact": impact, "severeImpact": severeImpact}

def solve(data, multiplier):
    days = nomilise(data['timeToElapse'], data['periodType'])
    reportedCases = int(data['reportedCases'])
    totalHospitalBeds = int(data['totalHospitalBeds'])
    avgDailyIncomePopulation = float(data['region']['avgDailyIncomePopulation'])
    avgDailyIncomeInUSD = float(data['region']['avgDailyIncomeInUSD'])
    factor = int(days / 3)
    currentlyInfected = reportedCases * int(multiplier)
    infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))

    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((totalHospitalBeds * 0.35) - severeCasesByRequestedTime)

    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = int((infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / days)

    return {"currentlyInfected": currentlyInfected, \
            "infectionsByRequestedTime": infectionsByRequestedTime, \
            "severeCasesByRequestedTime": severeCasesByRequestedTime, \
            "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime, \
            "casesForICUByRequestedTime": casesForICUByRequestedTime, \
            "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime, \
            "dollarsInFlight": dollarsInFlight
    }

input={
    'region': {
    'name': "Africa",
    'avgAge': 19.7,
    'avgDailyIncomeInUSD': 5,
    'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
    }

d = estimator(input)
print(d)

