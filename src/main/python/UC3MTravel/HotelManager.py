import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
import datetime
import hashlib

class HotelManager:
    def __init__(self):
        pass

    def validate_credit_card( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def read_data_from_json( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validate_credit_card(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req

    def room_reservation(self, credit_card, name_surname, id_Card, phone_number,
                         room_type, arrival_date, num_days):

        json_info = {
            "id_card": id_Card,
            "name_surname": name_surname,
            "credit_card": credit_card,
            "phone_number": phone_number,
            "reservation_date": datetime.datetime.now(),
            "arrival_date": arrival_date,
            "num_days": num_days,
            "room_type": room_type
        }

        def validate_name(name):

            if len(name) > 50 or len(name) < 10:
                return False

            name_array = name.split(' ')
            if len(name_array) != 2:
                return False

            return True

        def validate_number(phone_number):
            if len(phone_number) != 9:
                return False

            if not phone_number.isdigit():
                return False

            return True

        def validate_room(room_type):
            valid_rooms = ['single', 'double', 'suite']

            if room_type not in valid_rooms:
                return False

            return True

        def validate_date(date):
            if len(date) != 10:
                return False

            date_array = date.split('/')

            if len(date_array) != 3:
                return False

            if not date_array[0].isdigit() or not date_array[1].isdigit() or not date_array[2].isdigit():
                return False

            if int(date_array[0]) < 1 or int(date_array[0]) > 31:
                return False

            if int(date_array[1]) < 1 or int(date_array[1]) > 12:
                return False

            return True

        def validate_days(num_days):

            if not num_days.isdigit() or int(num_days) < 1 or int(num_days) > 10:
                return False

            return True

        def luhn_verification(card_number):

            # pulls the individual digits out of a number and returns them in an array
            def digits_of(n):
                return [int(d) for d in str(n)]

            digits = digits_of(card_number)

            # odd_indexed digits started from the first from the right, not multiplied by 2
            non_dupe_digits = digits[-1::-2]

            # even_indexed digits started from second from right, multiplied by 2 before added
            duplicated_digits = digits[-2::-2]

            # checksum stores all the digits and will be the number checked for divisibility by 10
            checksum = sum(non_dupe_digits)

            # multiply number by 2, if it is greater than 9, add the two digits together before adding
            for d in duplicated_digits:
                checksum += sum(digits_of(d * 2))

            # if rightmost digit is a 0, number is valid by Luhn's checksum algorithm.
            return checksum % 10

        def is_valid_credit_card(card_number):
            return luhn_verification(card_number) == 0


        # raise exceptions if the parameters are not valid
        if len(credit_card) != 16:
            raise HotelManagementException("credit card fails")
        elif not is_valid_credit_card(credit_card):
            raise HotelManagementException("credit card fails")
        elif not validate_number(phone_number):
           raise HotelManagementException("phone error")
        elif not validate_room(room_type):
           raise HotelManagementException("room error")
        elif not validate_name(name_surname):
           raise HotelManagementException("name error")
        elif not validate_days(num_days):
           raise HotelManagementException("day error")
        elif not validate_date(arrival_date):
           raise HotelManagementException("date error")
        value = "HotelReservation:" + json_info.__str__()
        return hashlib.md5(value.encode()).hexdigest()
