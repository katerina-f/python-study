
import asyncio
import time


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

data_dict = {}

class WrongCommand(Exception):
    pass

class ClientServerProtocol(asyncio.Protocol):

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

        if payload == "*":
            for key in data_dict:
                data += f"{data_dict[key][0]} {data_dict[key][1]} {key}\n"

        for key in data_dict:
            if data_dict[key][0] == payload:
                    data += f"{payload} {data_dict[key][1]} {key}\n"

            else:
                data

        return data + "\n"

    def put(self, payload):
        print(payload)
        metric, metric_value, timestamp = payload.split()
        print(metric, metric_value, timestamp)
        if timestamp not in data_dict:
            data_dict[timestamp] = [metric, metric_value]
        else:
            data_dict[timestamp] = [metric, metric_value]


        print(data_dict)
        return data_dict

#un_server("127.0.0.1", 8888)
