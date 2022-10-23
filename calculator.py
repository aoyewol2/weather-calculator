# This program calculates windchill and humidex based on user input

import math

# humid ranges
lowHum = 'Little or no discomfort.' # 20 to 29
midHum = 'Some discomfort.' # 30 to 39
highHum = 'Great discomfort. Avoid exertion.' # 40 to 44
vhHum = 'Dangerous. Heat stroke possible.' # 45+

# wind chill ranges
lowChill = 'Low risk.' # 0 to -9
modChill = 'Moderate risk.' # -10 to -27
highChill = 'High Risk. Skin can freeze in 10-30 minutes.' # -28 to -39
vhChill = 'Very High Risk. Skin can freeze in under 10 minutes.' # below -40

print('Welcome to weather calculator!\n--')
# while loop for reoccurring user input
answer = True
while answer:
    # initial input
    temp = float(input('Enter a temperature between -50 and 50: '))
    # temperature section
    while temp > 50 or temp < -50:
        # invalid input, prompt again
        print('That temperature is invalid.')
        temp = float(input('Enter a temperature between -50 and 50: '))

    # windchill section
    if temp <= 0:
        print('Calculating windchill.')
        windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))
        # input validation using while loop
        while windSpeed < 1 or windSpeed > 99:
            print('That wind speed is invalid.')
            windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))

        # windchill calculation
        if windSpeed >= 1 or windSpeed <= 99:
            windChill = 13.12 + 0.6125 * temp - 11.37 * (windSpeed ** 0.16) + 0.3965 * temp * (windSpeed ** 0.16)
            windChill = round(windChill)

            # windchill output statements
            if 0 >= windChill >= -9:
                print('The windchill is {}. {}'.format(windChill,lowChill))
            elif -10 >= windChill >= -27:
                print('The windchill is {}. {}'.format(windChill, modChill))
            elif -28 >= windChill >= -39:
                print('The windchill is {}. {}'.format(windChill, highChill))
            else:
                print('The windchill is {}. {}'.format(windChill, vhChill))

    # humidex section
    elif temp >= 20:
        print('Calculating humidex.')
        dewPoint = float(input('Enter the dewpoint between -50 and 50: '))
        # input validation using while loop
        while dewPoint > temp or dewPoint > 50 or dewPoint < -50:
            print('That dew point is invalid.')
            dewPoint = float(input('Enter the dewpoint between -50 and 50: '))

        # dewpoint calculation
        if dewPoint < temp or dewPoint <= 50 or dewPoint >= -50:
            F = 6.11 * math.exp(5417.7530 * (1 / 273.16 - 1 / (273.16 + dewPoint)))
            G = 5 / 9 * (F-10)
            humidex = temp + G
            humidex = round(humidex)

            # humidex output statements
            if 20 <= humidex <= 29:
                print('The humidex is {}. {}'.format(humidex, lowHum))
            elif 30 <= humidex <= 39:
                print('The humidex is {}. {}'.format(humidex, midHum))
            elif 40 <= humidex <= 44:
                print('The humidex is {}. {}'.format(humidex, highHum))
            elif humidex >= 45:
                print('The humidex is {}. {}'.format(humidex, vhHum))
        else:
            print('That dew point is invalid.')
            dewPoint = float(input('Enter the dewpoint between -50 and 50: '))

    # if neither conditions are true
    else:
        print('Windchill and humidex are not a factor at this temperature.')

    # ask to run program again after calculations finish
    answer = input('Check another weather condition (Y/N)? ').lower()  # add lower.() so N and n inputs are accepted
    while answer.lower() != "y" and answer.lower() != "n":
        print('That input is invalid.')
        answer = input('Check another weather condition (Y/N)? ')
    if answer.lower() == 'y':
        print('--')
        continue
    elif answer.lower() == 'n':
        print('--')
        print('Goodbye!')
        exit(0)
