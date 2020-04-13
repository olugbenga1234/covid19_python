# convert period type
def nomilise(timeToElapse, periodType):
    period = 0
    if periodType == "days":
        period = timeToElapse
    elif periodType == "weeks":
        period = timeToElapse * 7
    elif periodType == "months":
        period = timeToElapse * 30
    return int(period)

def estimator(data):

    impact = solve(data, 10)
    severeImpact = solve(data, 50)

    return {"data": data, "impact": impact, "severeImpact": severeImpact}

def solve(data, multiplier):
    days = nomilise(data['timeToElapse'], data['periodType'])
    reportedCases = int(data['reportedCases'])
    totalHospitalBeds = int(data['totalHospitalBeds'])
    earnByPeople = int(data['region']['avgDailyIncomePopulation'])
    USDEarn = int(data['region']['avgDailyIncomeInUSD'])
    factor = int(days / 3)
    currentlyInfected = reportedCases * int(multiplier)
    infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))

    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((totalHospitalBeds * 0.35) - severeCasesByRequestedTime)

    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = int((infectionsByRequestedTime * earnByPeople * USDEarn) / days)

    return {"currentlyInfected": currentlyInfected, \
            "infectionsByRequestedTime": infectionsByRequestedTime, \
            "severeCasesByRequestedTime": severeCasesByRequestedTime, \
            "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime, \
            "casesForICUByRequestedTime": casesForICUByRequestedTime, \
            "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime, \
            "dollarsInFlight": dollarsInFlight
    }

