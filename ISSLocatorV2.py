import urllib.request, json, turtle, time

while True:
    universal_url = 'http://api.open-notify.org/'
    astronaut_url = universal_url + 'astros.json'
    ISS_now_url = universal_url + 'iss-now.json'
    ISS_pass_url = universal_url + 'iss-pass.json?lat=25.75&lon=-80.37'


    #*-*-*-*-*-*-*-*-*-*-*
    # Astronauts in space
    #*-*-*-*-*-*-*-*-*-*-*
    astronauts = urllib.request.urlopen(astronaut_url)
    astronaut_result = json.loads(astronauts.read())

    f = open('Astronauts.txt', 'w')

    f.write("People in space: %s \n"%str(astronaut_result['number']))

    for p in astronaut_result['people']:
        f.write(p['name'] + "\n")

    f.close()

    #*-*-*-*-*-*-*
    # ISS Locator
    #*-*-*-*-*-*-*

    ISS_now_response = urllib.request.urlopen(ISS_now_url)
    ISS_now_result = json.loads(ISS_now_response.read())

    location = ISS_now_result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])


    #Setting up the screen
    screen = turtle.Screen()
    screen.setup(720,360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    #Plotting the ISS image
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)

    iss.penup()
    iss.goto(lon, lat)

    #*-*-*-*-*-*-*
    # ISS Locator
    #*-*-*-*-*-*-*

    fiu_lat = 25.7514312
    fiu_lon = -80.37142170000001

    fiu_location = turtle.Turtle()
    fiu_location.penup()
    fiu_location.color('yellow')
    fiu_location.goto(fiu_lon,fiu_lat)
    fiu_location.dot(5)
    fiu_location.hideturtle()

    ISS_pass_response = urllib.request.urlopen(ISS_pass_url)
    ISS_pass_result = json.loads(ISS_pass_response.read())

    over = ISS_pass_result['response'][1]['risetime']
    style = ['Arial', 8, 'bold']
    fiu_location.write(time.ctime(over), font = style)

    time.sleep(60)
