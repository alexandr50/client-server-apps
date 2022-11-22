import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(client):


    encoded_response = client.recv(MAX_PACKAGE_LENGTH)

    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError



def send_message(socket, message):

    if not isinstance(message, dict):
        raise TypeError
    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    socket.send(encoded_message)
    


