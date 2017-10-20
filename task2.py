from weather import Weather
#get the next five day weather in newlist according to forecast method:
def forecast(city):
 weather = Weather()
 location = weather.lookup_by_location(city)
 condition = location.condition()
 forecast = location.forecast()
 i = 0
 newlist = []
 while i < 5:
  newlist.append(forecast[i])
  i+=1
 # the initial d which contains the highest and lowest temperature, and the rainday list
 d = {'high':newlist[0]['high'],'low':newlist[0]['low'],'rain':[]}
 for j in newlist:
  if j['high']>=d['high']:
   d['high'] = j['high']
 for j in newlist:
  if j['low'] <=d['low']:
   d['low'] = j['low']
 for j in newlist:
  if j['text'] == 'Showers' or 'rain' in j['text']:
   d['rain'].append(j['date'])
 #if no rains in next 5 days, inform users, if rains, give the dates list has rains
 if d['rain'] == []:
  d['rain'] = 'No rains in the next five days'
 #give the exact date with the highest temperature in d, the lowest temperature is similar
 for j in newlist:
  if j['high'] == d['high']:
   d['high'] = j['date']
 for j in newlist:
  if j['low'] == d['low']:
   d['low'] = j['date']
 return d
print(forecast('halifax'))
