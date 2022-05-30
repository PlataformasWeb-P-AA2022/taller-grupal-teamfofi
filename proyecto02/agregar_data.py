from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Matricula

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Matricula
matricula1 = Matricula(nombrePropietario="Tony", placa="LAA5454", \
        anio="2012",costo=200.20)

matricula2 = Matricula(nombrePropietario="Tony", placa="LAA5454", \
        anio="2012",costo=200.20)

matricula3 = Matricula(nombrePropietario="Tony", placa="LAA5454", \
        anio="2012",costo=200.20)

matricula4 = Matricula(nombrePropietario="Tony", placa="LAA5454", \
        anio="2012",costo=200.20)

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(matricula1)
session.add(matricula2)
session.add(matricula3)
session.add(matricula4)

# se confirma las transacciones
session.commit()
