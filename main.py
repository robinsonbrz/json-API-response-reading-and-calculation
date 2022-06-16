import json

f = open('api-response.json')

# JSON object as a dictionary
setData = json.load(f)


def calculate_ratio(year, id, data):
    '''
    it accepts id and year as string or integer
    returns a dictionary with calculated
    MarketValue = {cost} * {marketRatio}
    AuctionValue = {cost} * {auctionRatio}
    when id and year is found in a given data

    returns false if theres no match for id and year
    returns false if there is some id or year diferent from string or integer
    '''

    # checks for empty string returns false without wasting time
    if (id == '') or (year == ''):
        print("Invalid parameters")
        return False

    # if input is an int it can be converted to valid set and year
    if (isinstance(id, int)):
        id = str(id)

    if (isinstance(year, int)):
        year = str(year)
    
    # at this poit we must have a str otherwise
    # returns false without wasting time
    if not(isinstance(id, str)) or not(isinstance(year, str)):
        print("Invalid parameters")
        return False

    cost = ''
    for k1 in data:
        if (k1 == id):
            cost = data[k1]['saleDetails']['cost']
            for k2 in data[k1]['schedule']['years']:
                if(year in k2):
                    marketRatio = data[k1]['schedule']['years'][year]['marketRatio']
                    auctionRatio = data[k1]['schedule']['years'][year]['auctionRatio']
                    marketValue = float(cost) * float(marketRatio)
                    auctionValue = float(cost) * float(auctionRatio)
                    values = {
                        'marketValue': marketValue,
                        'auctionValue': auctionValue
                    }
                    return(values)
            return False
    return False


print('\n\nYear 2007 ID 67352')
print(calculate_ratio(2007, 67352, setData))
print(calculate_ratio(2007, '67352', setData))
print(calculate_ratio('2007', 67352, setData))
print(calculate_ratio('2007', '67352', setData))


print('\n\nYear 2011 ID 87964')
print(calculate_ratio(2011, 87964, setData))
print(calculate_ratio(2011, '87964', setData))
print(calculate_ratio('2011', 87964, setData))
