import socket
import time

class Client:
    def __init__(self, host, port, timeout = None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.connect((host,port))
        self.sock.settimeout(timeout)

    def get(self, metric):
        message = bytes(f"get {metric}\n", encoding = "UTF-8")
        self.sock.send(message)
        data = self.sock.recv(1024).decode("UTF-8")
        expected_answer = "ok\n\n"
        data = data.split("\n")

        data_metrics = []
        dict_of_metrics = {}
        tuple_of_values = ()
        i = 0

        if data == expected_answer:
            try:
                dict_of_metrics = {}
            except IndexError:
                pass


        for value in data:
            if value != "ok":
                value = value.split(" ")
                data_metrics.append(value)

        if metric == "*":
            i = 0
            try:
                while i <= len(data_metrics):
                    for value in data_metrics:
                        tuple_of_values = int(value[2]),float(value[1])
                        if value[0] in dict_of_metrics.keys():
                            dict_of_metrics[value[0]].append(tuple_of_values)
                            dict_of_metrics[value[0]].sort()
                        else:
                            dict_of_metrics[value[0]] = []
                            dict_of_metrics[value[0]].append(tuple_of_values)
                            dict_of_metrics[value[0]].sort()

            except IndexError:
                pass
            i += 1

        else:
            i = 0
            try:
                while i <= len(data_metrics):
                    dict_of_metrics[metric] = []
                    for value in data_metrics:
                        tuple_of_values = int(value[2]),float(value[1])
                        if metric in dict_of_metrics.keys():
                            dict_of_metrics[metric].append(tuple_of_values)
                            dict_of_metrics[metric].sort()
                        else:
                            dict_of_metrics[metric].append(tuple_of_values)
                            dict_of_metrics[metric].sort()
            except IndexError:
                pass
            i += 1
        return dict_of_metrics


    def put(self, metric, metric_value, timestamp = None):
            if timestamp == None:
                timestamp = str(int(time.time()))
            metric = str(metric)
            metric_value = float(metric_value)
            timestamp = str(int(timestamp))
            #send data like - put palm.cpu 10.6 1501864247\n
            expected_answer = "ok\n\n"
            unexpected_answer = "error\nwrong command\n\n"
            message = bytes(f"put {metric} {metric_value} {timestamp}\n", encoding = "UTF-8")
            self.sock.send(message)
            data = self.sock.recv(1024).decode("UTF-8")

            if data == expected_answer:
                pass
            elif data == unexpected_answer:
                raise ClientError

class ClientError:
    pass

#client = Client("127.0.0.1", 8888, timeout=15)

#client.put("palm.cpu", 0.5, timestamp=1150864247)
#client.put("palm.cpu", 2.0, timestamp=1150864248)
#client.put("palm.cpu", 0.5, timestamp=1150864248)

#client.put("eardrum.cpu", 3, timestamp=1150864250)
#client.put("eardrum.cpu", 4, timestamp=1150864251)
#client.put("eardrum.memory", 4200000)

#print(client.get("*"))
