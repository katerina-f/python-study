
import asyncio


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class WrongCommand(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.data_dict = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        try:
            resp = self.process_data(data.decode())
        except WrongCommand as err:
            resp = 'error\nwrong command\n\n'
        finally:
            self.transport.write(resp.encode())

    def process_data(self, data):

        status, payload = data.split(" ", 1)
        payload = payload.strip()

        if status == "get":
            data_for_client = self.get(payload)
            return data_for_client

        if status == "put":
            self.put(payload)
            return "ok\n\n"
        else:
            raise WrongCommand


    def get(self, payload):
        data = "ok\n"

        for key in self.data_dict:
            if key == payload:
                for metric_value in self.data_dict[key]:
                    data += f"{payload} {metric_value[0]} {metric_value[1]}\n"

            if payload == "*":
                for metric_value in self.data_dict[key]:
                    data += f"{key} {metric_value[0]} {metric_value[1]}\n"

            else:
                data

        return data + "\n"

    def put(self, payload):
        metric, metric_values = payload.split(" ", 1)
        metric_values = metric_values.split(' ')
        metric_values = metric_values[0], metric_values[1]
        if metric not in self.data_dict:
            self.data_dict[metric] = []
            self.data_dict[metric].append(metric_values)
        else:
            self.data_dict[metric].append(metric_values)
        return self.data_dict

run_server("127.0.0.1", 8888)
