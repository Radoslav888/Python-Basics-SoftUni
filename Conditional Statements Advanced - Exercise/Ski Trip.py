days = int(input())
room = str(input())
grade = str(input())
days -= 1
room_1 = 18 * days
apt = 25 * days
president_apt = 35 * days

if room == "room for one person":
    if grade == 'positive':
        room_1 = room_1 + (room_1 * 0.25)
    elif grade == 'negative':
        room_1 = room_1 - (room_1 * 0.10)
    print(f'{room_1:.2f}')
if room == "apartment" and days < 10:
    apt *= 0.7
    if grade == 'positive':
        apt = apt + (apt * 0.25)
    elif grade == 'negative':
        apt = apt - (apt * 0.10)
    print(f'{apt:.2f}')
elif room == "apartment" and 10 < days < 15:
    apt *= 0.65
    if grade == 'positive':
        apt = apt + (apt * 0.25)
    elif grade == 'negative':
        apt = apt - (apt * 0.10)
    print(f'{apt:.2f}')
elif room == "apartment" and 15 < days:
    apt *= 0.50
    if grade == 'positive':
        apt = apt + (apt * 0.25)
    elif grade == 'negative':
        apt = apt - (apt * 0.10)
    print(f'{apt:.2f}')
if room == "president apartment" and days < 10:
    president_apt *= 0.9
    if grade == 'positive':
        president_apt = president_apt + (president_apt * 0.25)
    elif grade == 'negative':
        president_apt = president_apt - (president_apt * 0.10)
    print(f'{president_apt:.2f}')
elif room == "president apartment" and 10 < days < 15:
    president_apt *= 0.85
    if grade == 'positive':
        president_apt = president_apt + (president_apt * 0.25)
    elif grade == 'negative':
        president_apt = president_apt - (president_apt * 0.10)
    print(f'{president_apt:.2f}')
elif room == "president apartment" and 15 < days:
    president_apt *= 0.80
    if grade == 'positive':
        president_apt = president_apt + (president_apt * 0.25)
    elif grade == 'negative':
        president_apt = president_apt - (president_apt * 0.10)
    print(f'{president_apt:.2f}')


