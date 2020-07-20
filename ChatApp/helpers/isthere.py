def is_there_room(cache,room_name):

    if not cache.get(room_name):
        cache[room_name] = []

    return cache

def is_there_client(ws_client,room_name):

    if not ws_client.get(room_name):
        ws_client[room_name] = set()

    return ws_client
    