import requests
#pip install requests

TEST_MAP_NAME = 'H7S4SportsmansWarehouse.catalog.Oracle.fromSIPv7.toFixedLengthFlatFile.write'


def get_token(method_username, method_password):
    method_response = requests.post('/'.join(["https://id.spsc.io/identity", 'token/']),
                                    json={'grant_type': 'password',
                                          'username': method_username,
                                          'password': method_password,
                                          'client_id': '595'})
    return method_response.json()['access_token']


def get_new_token_every_time(method_username, method_password):
    delete_token(method_username, method_password)
    return get_token(method_username, method_password)


def delete_token(method_username, method_password):
    method_response = requests.delete('/'.join(["https://id.spsc.io/identity", 'token/']),
                                      json={'grant_type': 'password',
                                            'username': method_username,
                                            'password': method_password,
                                            'client_id': '595'})
    return method_response


def get_username_pass():
    method_username = input('Username: ')
    method_password = input('Password: ')
    return method_username, method_password


def get_log_for_map(map_name, token):
    return requests.get("https://xd.spsc.io/xd/" + 'log/' + map_name + '/master', headers={'X-Authorization-Token': token})


if __name__ == '__main__':
    username, password = get_username_pass()
    print ("Here is the token")
    print (get_token(username, password))
    print ("\n\n")
    my_response = get_log_for_map(TEST_MAP_NAME, get_new_token_every_time(username, password))
    data = my_response.json()
    print('got it' + str(my_response), "\n\n")

    for entry in data["result"]:
        print (entry)
        print ("Author:", entry["Author"])
        print ("Message:", entry["message"], "\n\n\n")

