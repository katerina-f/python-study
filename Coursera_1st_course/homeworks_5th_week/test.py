import time

class Client:
    def __init__(self, host, port, timeout = None):
        self.host = str(host)
        self.port = int(port)
        self.timeout = timeout

    def get(self, metric, metric_value, timestamp = None):
        message = f"get {metric}\n"
        expected_answer = "ok\n\n"

        data = f"ok\n{metric},{metric_value},{timestamp}\nok\n{metric} {metric_value} {timestamp}\n"

        data = data.split("\n")
        data_metrics = []
        dict_of_metrics = {}
        tuple_of_values = ()
        i = 0
        for value in data:
            if value != "ok":
                value = value.split(" ")
                data_metrics.append(value)


        if metric == "*":
            i = 0
            try:
                while i <= len(data_metrics):
                    print(i)
                    print(data_metrics)
                    for value in data_metrics:
                        tuple_of_values = value[1],value[2]
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

            print(dict_of_metrics)

        while i <= len(data_metrics):
            dict_of_metrics[metric] = []
            for value in data_metrics:
                if metric == value[0]:
                    tuple_of_values = value[1],value[2]
                    if metric in dict_of_metrics.keys():
                        dict_of_metrics[metric].append(tuple_of_values)
                    else:
                        dict_of_metrics[metric].append(tuple_of_values)
                else:
                    pass
            i += 1
            return dict_of_metrics


client = Client("127.0.0.1", 8888, timeout=15)

print(client.get("*", 0.5, timestamp=1150864247))
print(client.get("palm.cpu", 2.0, timestamp=1150864248))
print(client.get("palm.cpu", 0.5, timestamp=1150864248))
