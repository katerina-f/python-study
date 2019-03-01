import csv
import os

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        try:
            file_ext = os.path.splitext(self.photo_file_name)
        except:
            file_ext = ""
        return file_ext


class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        if body_whl == "":
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
        else:
            self.body_whl = body_whl.split("x")
            self.body_width = float(self.body_whl[0])
            self.body_height = float(self.body_whl[1])
            self.body_length = float(self.body_whl[2])

    def get_body_volume(self):
        body_volume = self.body_height*self.body_length*self.body_width
        return body_volume


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) #пропускаем заголовок
        obj_list = []
        for row in reader:
            obj_dict = {}
            try:
                obj_dict["car_type"] = row[0]
                obj_dict["brand"] = row[1]
                obj_dict["passenger_seats_count"] = row[2]
                obj_dict["photo_file_name"] = row[3]
                obj_dict["body_whl"] = row[4]
                obj_dict["carrying"] = row[5]
                obj_dict["extra"] = row[6]
                obj_list.append(obj_dict)
            except IndexError:
                pass
    for obj_dict in obj_list:
        try:
            if obj_dict["car_type"] == "car":
                car = Car(car_type = obj_dict["car_type"], brand = obj_dict["brand"], photo_file_name = obj_dict["photo_file_name"], carrying = float(obj_dict["carrying"]), passenger_seats_count = int(obj_dict["passenger_seats_count"]))
                car_list.append(car)
            if obj_dict["car_type"] == "truck":
                truck = Truck(car_type = obj_dict["car_type"], brand = obj_dict["brand"], photo_file_name = obj_dict["photo_file_name"], carrying = float(obj_dict["carrying"]), body_whl = obj_dict["body_whl"])
                car_list.append(truck)
            if obj_dict["car_type"] == "spec_machine":
                spec_machine = SpecMachine(car_type = obj_dict["car_type"], brand = obj_dict["brand"], photo_file_name = obj_dict["photo_file_name"], carrying = float(obj_dict["carrying"]), extra = obj_dict["extra"])
                car_list.append(spec_machine)
        except IndexError:
            pass
    return car_list

#list = get_car_list("coursera_week3_cars.csv")
#for car in list:
    #print(car.__dict__)
