from deploy_handlers import deploy_helper as dh
import Utils.utils as u
import socket


def main():
    handle_options()


def handle_options():
    option = -1

    while option != 0:
        option = request_options()
        if option == 0:
            print("Proceso terminado")
        elif option == 1:
            dh.deploy_db()
            # dh.deploy_portainer()
        elif option == 2:
            dh.stop_db()
            # dh.deploy_portainer()
        elif option == 3:
            address_db = request_address("DB")
            address_back = request_address("BACK")
            dh.deploy_front(address_db, address_back)
        elif option == 4:
            dh.stop_front()
        elif option == 5:
            address_db = request_address("DB")
            address_front = request_address("FRONT")
            dh.deploy_back(address_db, address_front)
        elif option == 6:
            dh.stop_back()
        elif option == 7:
            dh.deploy_db()
            address_db = request_address("DB")
            address_back = request_address("BACK")
            dh.deploy_front(address_db, address_back)
            address_db = request_address("DB")
            address_front = request_address("FRONT")
            dh.deploy_back(address_db, address_front)
        elif option == 8:
            dh.stop_db()
            dh.stop_front()
            dh.stop_back()
        elif option == 9:
            dh.deploy_portainer()
        elif option == 10:
            dh.stop_portainer()


def request_options():
    option = ""
    while option not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("Por favor, seleccione los servicios a desplegar/parar:\n")
        print("[0]...................Salir")
        print("[1]...................Desplegar servicios de Base de Datos")
        print("[2]...................Parar servicios de Base de Datos")
        print("[3]...................Desplegar servicios de Frontal")
        print("[4]...................Parar servicios de Frontal")
        print("[5]...................Desplegar servicios de Backend")
        print("[6]...................Parar servicios de Backend")
        print("[7]...................Desplegar todos los servicios")
        print("[8]...................Parar todos los servicios")
        print("[9]...................Desplegar solo el Portainer")
        print("[10]..................Parar solo el Portainer\n")
        option = input()
        if option not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Opción invalida, por favor seleccione una opción de la lista")
        else:
            return int(option)


def request_address(machine):
    address = ""
    while not u.is_valid_address(address):
        print("Inserta la IP o el DNS donde se ha desplegado los servicios de la maquina %s (si esta vacío se asumirá localhost):" % machine)
        address = input()
        if address == "":
            address = u.get_private_ip_address()
            # address = "192.168.1.27"
            print("\t...Usada localhost [%s] para maquina %s" % (address, machine))
        elif not u.is_valid_address(address):
            print("\t...Formato de dirección: %s para la maquina %s no valido" % address, machine)
        else:
            print("\t...Usada IP [%s] para maquina %s" % (address, machine))
    return address


if __name__ == "__main__":
    main()