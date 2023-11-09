import flask
from flask import request

import grpc
import kvstore_pb2, kvstore_pb2_grpc
from google.protobuf import any_pb2, wrappers_pb2

def init_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = kvstore_pb2_grpc.KVStoreStub(channel)
    return stub

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False
stub = init_stub()

@app.route('/')
def SDCS():
    return 'Simple Distributed Cache System\n', 200

@app.route('/', methods=['POST'])
def Set():
    data = request.json
    key, value = list(data.items())[0]

    any_value = any_pb2.Any()

    if isinstance(value, str):
        wrappers_value = wrappers_pb2.StringValue(value=value)
        any_value.Pack(wrappers_value)
    elif isinstance(value, int):
        wrappers_value = wrappers_pb2.Int32Value(value=value)
        any_value.Pack(wrappers_value)
    elif isinstance(value, bool):
        wrappers_value = wrappers_pb2.BoolValue(value=value)
        any_value.Pack(wrappers_value)
    elif isinstance(value, list):
        # TODO
        pass
    elif isinstance(value, float):
        wrappers_value = wrappers_pb2.FloatValue(value=value)
        any_value.Pack(wrappers_value)
    elif isinstance(value, dict):
        # TODO
        pass
    else:
        # TODO
        pass

    stub.Set(kvstore_pb2.SetRequest(key=key, value=any_value))
    return '', 200

@app.route('/<key>', methods=['GET'])
def Get(key):
    response = stub.Get(kvstore_pb2.GetRequest(key=key))

    if response.value is not None:
        any_value = response.value

        str_value = wrappers_pb2.StringValue()
        if any_value.Unpack(str_value):
            return '{{"{key}":"{value}"}}\n'.format(key=key, value=str_value.value), 200

        int_value = wrappers_pb2.Int32Value()
        if any_value.Unpack(int_value):
            return '{{"{key}":{value}}}\n'.format(key=key, value=int_value.value), 200

        bool_value = wrappers_pb2.BoolValue()
        if any_value.Unpack(bool_value):
            return '{{"{key}":{value}}}\n'.format(key=key, value=bool_value.value), 200

        float_value = wrappers_pb2.FloatValue()
        if any_value.Unpack(float_value):
            return '{{"{key}":{value}}}\n'.format(key=key, value=float_value.value), 200

        # list
        # dict
        # None
        # TODO
        return '', 404
    else:
        return '', 404

@app.route('/<key>', methods=['DELETE'])
def Remove(key):
    response = stub.Remove(kvstore_pb2.RemoveRequest(key=key))
    if response.success:
        return '1\n'
    else:
        return '0\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)