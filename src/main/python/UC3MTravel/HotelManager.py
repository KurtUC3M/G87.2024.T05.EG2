import json
from HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
import datetime
import hashlib

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReaddatafromJSOn( self, fi):

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
        if not self.validatecreditcard(c):
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

        # raise exceptions if the parameters are not valid
        if len(credit_card) != 16:
            raise HotelManagementException("credit card fails")
        value = "HotelReservation:" + json_info.__str__()
        return hashlib.md5(value.encode()).hexdigest()
