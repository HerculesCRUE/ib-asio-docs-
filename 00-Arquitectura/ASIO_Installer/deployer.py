from deploy_handlers import deploy_helper as dh
import Utils.utils as u
import socket


def main():
    handle_options()


def handle_options():
    option = request_options()
    if option == 1:
        dh.deploy_db()
        dh.deploy_portainer()
    if option == 2:
        address_db = request_address("DB")
        address_back = request_address("BACK")
        dh.deploy_front(address_db, address_back)
    elif option == 5:
        dh.deploy_portainer()


def request_options():
    option = ""
    while option not in ["1", "2", "3", "4", "5"]:
        print("Por favor, seleccione los servicios que quieres desplegar:")
        print("\t1 -> Desplegar servicios de Base de Datos")
        print("\t2 -> Desplegar servicios de Frontal")
        print("\t3 -> Desplegar servicios de Backend")
        print("\t4 -> Desplegar todos los servicios")
        print("\t5 -> Desplegar solo el Portainer")
        option = input()
        if option not in ["1", "2", "3", "4", "5"]:
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
            print("\t...Usada localhost [%s] para maquina %s" % (address, machine))
        elif not u.is_valid_address(address):
            print("\t...Formato de dirección: %s para la maquina %s no valido" % address, machine)
        else:
            print("\t...Usada IP [%s] para maquina %s" % (address, machine))
    return address


if __name__ == "__main__":
    main()