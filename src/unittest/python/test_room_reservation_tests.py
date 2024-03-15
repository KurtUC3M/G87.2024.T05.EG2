from unittest import TestCase

from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException


class TestRoomReservation(TestCase):

    def setUp(self):
        pass
    def test_hotel_reservation_ok(self):
        pass

    def test_room_reservation_valid(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doers",
                                                    id_Card= "12345", phone_number="123456789",
                                                    room_type = "double",
                                                    arrival_date= "21/03/2024", num_days="2")

            print(value, "pass 1")
            self.assertEqual(value, "")

        print(cm.exception)

    def test_room_reservation_invalid_card(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105101",
                                                name_surname="Jane Doe",
                                                id_Card= "12345", phone_number="123456789",
                                                room_type = "double",
                                                arrival_date= "21/03/2024", num_days="2")

            self.assertEqual(value, "")

        print(cm.exception, "pass 2")

    def test_room_reservation_invalid_name(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doe",
                                                    id_Card= "12345", phone_number="123456789",
                                                    room_type = "double",
                                                    arrival_date= "21/03/2024", num_days="2")

            self.assertEqual(value, "")

        print(cm.exception, "pass 3")

    def test_room_reservation_invalid_phone(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doers",
                                                    id_Card= "12345", phone_number="1234567891",
                                                    room_type = "double",
                                                    arrival_date= "21/03/2024", num_days="2")

            self.assertEqual(value, "")

        print(cm.exception, "pass 4")

    def test_room_reservation_invalid_room(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doers",
                                                    id_Card= "12345", phone_number="123456789",
                                                    room_type = "doubles",
                                                    arrival_date= "21/03/2024", num_days="2")

            self.assertEqual(value, "")

        print(cm.exception, "pass 5")

    def test_room_reservation_invalid_date(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doers",
                                                    id_Card= "12345", phone_number="123456789",
                                                    room_type = "double",
                                                    arrival_date= "21/032024", num_days="2")

            self.assertEqual(value, "")

        print(cm.exception, "pass 6")

    def test_room_reservation_invalid_days(self):
        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as cm:
            value = my_reservation.room_reservation(credit_card = "5105105105105100",
                                                    name_surname="Jane Doers",
                                                    id_Card= "12345", phone_number="123456789",
                                                    room_type = "double",
                                                    arrival_date= "21/03/2024", num_days="0")

            self.assertEqual(value, "")

        print(cm.exception, "pass 7")

