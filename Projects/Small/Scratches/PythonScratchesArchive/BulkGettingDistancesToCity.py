"""
----------------------------------------------------------------------------------------
  OVERVIEW


  Date created: 22.06.2023
  I wrote this simple script to find the city nearest to me.
  I had a list of cities, and I had to sort these cities from the closest to \
  the farthest to a set location.


----------------------------------------------------------------------------------------
"""

from base64 import b64encode
from hashlib import pbkdf2_hmac
from operator import itemgetter
from platform import node, processor
from time import sleep

from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from getmac import get_mac_address


def main() -> None:
    def count_cities(my_cities_dict: dict) -> int:
        cites_count: int = 0

        for count_outer_location in my_cities_dict:
            cites_count += len(my_cities_dict[count_outer_location])

        return cites_count

    def get_user_agent_id() -> str:
        password_str: str = f'K$92*3x{get_mac_address()}' \
                            f'9k$etv7s6aV&R2M@7v{node()}' \
                            f'%$85p2{processor()}925RYie'

        password_bytes: bytes = bytes(password_str, 'utf-8')

        salt: bytes = b'\xd7\xc1\x89w\xc09\t\xc5\x8a@X\x01f\x00\xfa\x95'
        times: int = 94558
        id_bytes: bytes = pbkdf2_hmac('sha512', password_bytes, salt, times)
        return b64encode(id_bytes).decode('utf-8')

    distances_decimal_places: int = 2
    my_city: str = 'Knurów, Silesia, Poland'
    wait_time: float = 1.5  # Nominatim's Terms of Service do not allow wait times \
    # below 1 seconds - "No heavy uses (an absolute maximum of 1 request per second)." \
    # https://operations.osmfoundation.org/policies/nominatim/

    # For demonstration purposes this list has been shortened from ~46 cities to 10.
    cities: dict = {
        r"Poland": (
            r"Bełchatów",
            r"Białystok",
            r"Bielsko-Biała",
            r"Bydgoszcz",
            r"Częstochowa",
            r"Gdańsk",
            "Gdynia",
            r"Gliwice",
            r"Gniezno",
            r"Gorzów Wielkopolski",
            r"Bad City Name Example"
        )
    }

    min_wait_time: float = 1

    if wait_time < min_wait_time:
        print(f"Stopped the Script!\nWait Time Below {min_wait_time} ({wait_time})!")
        return

    cities_amount: int = count_cities(cities)

    user_agent_id: str = get_user_agent_id()
    print(f"\nRunning Program with user_agent ID: {user_agent_id}\n")

    geolocator = Nominatim(user_agent=f'Python-GettingDistancesOf{cities_amount}Cities'
                                      f'_To{my_city.split(" ")[0].split(",")[0]}'
                                      f'_ID_{user_agent_id}')
    # Nominatim also requires a user_agent name for every Nominatim-using application.

    my_city_location = geolocator.geocode(my_city)

    if not my_city_location:
        print(f"Couldn't get the Location of '{my_city}'!")
        return

    sleep(wait_time)

    my_main_location_coordinates: tuple = (my_city_location.latitude,
                                           my_city_location.longitude)

    distances: list = []
    skipped_cities: list = []

    count: int = 0

    for outer_location in cities:
        for city in cities[outer_location]:
            count += 1

            print(f"{count}/{cities_amount}  |  Getting the city {city}",
                  end='')

            city_location = geolocator.geocode(f'{city}, {outer_location}')

            if not city_location:
                skipped_cities.append(f'{city}, {outer_location}')
                print("  |  CITY NOT FOUND!!! | SKIPPED!")
                continue

            city_coordinates: tuple = (city_location.latitude,
                                       city_location.longitude)

            distance = geodesic(my_main_location_coordinates,
                                city_coordinates).kilometers
            distances.append((city, distance))

            print(f"  |  Distance - {distance:.{distances_decimal_places}f} kilometers")

            sleep(wait_time)

    distances.sort(key=itemgetter(1))

    print('\n\n\n\n***************************\nThe sorted distances are: ')

    for i, city_info in enumerate(distances, start=1):
        print(f"{i}. {city_info[0]} - {city_info[1]:.{distances_decimal_places}f} "
              "kilometers")

    print('\nSkipped Cities:')

    for i, skipped_city in enumerate(skipped_cities, start=1):
        print(f'{i}. {skipped_city}')

    print('***************************')


if __name__ == '__main__':
    main()
