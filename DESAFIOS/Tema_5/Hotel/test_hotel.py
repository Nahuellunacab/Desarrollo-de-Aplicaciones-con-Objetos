import pytest
from hotel import Hotel, Habitacion, Estandar, Suite, SuitePremium

class TestHotel:
    
    @pytest.fixture
    def hotel(self):
        # Crea una instancia de Hotel usando el archivo habitaciones.csv antes de cada test que lo necesite
        return Hotel("habitaciones.csv")
    
    def test_constructor_hotel(self):
        # Prueba que el constructor de Hotel funcione y que haya 6 habitaciones cargadas
        hotel = Hotel("habitaciones.csv")
        assert hotel is not None
        assert len(hotel.cantidad_habitaciones()) == 6
    
    def test_constructor_archivo_inexistente(self):
        # Verifica que si el archivo no existe, se lance FileNotFoundError
        with pytest.raises(FileNotFoundError):
            Hotel("archivo_inexistente.csv")
    
    def test_cantidad_por_tipo(self, hotel):
        # Prueba que la cantidad de habitaciones por tipo sea la esperada
        cantidades = hotel.cantidad_por_tipo()
        assert cantidades == { "Estandar": 2, "Suite": 2, "SuitePremium": 2 }
    
    def test_habitacion_estandar(self):
        # Prueba el cálculo de costo para una habitación estándar
        habitacion = Estandar(101, "Juan Perez", 5000, 3, False)
        assert habitacion.calcular_costo() == 15000
    
    def test_suite_sin_vista_mar(self):
        # Prueba el cálculo de costo para una suite sin vista al mar
        suite = Suite(202, "Ana Martinez", 8200, 4, False)
        assert suite.calcular_costo() == 32800
    
    def test_suite_con_vista_mar(self):
        # Prueba el cálculo de costo para una suite con vista al mar
        suite = Suite(201, "Carlos Gomez", 8000, 5, True)
        assert suite.calcular_costo() == 44000
    
    def test_suite_premium_sin_jacuzzi(self):
        # Prueba el cálculo de costo para una suite premium sin jacuzzi
        suite_premium = SuitePremium(302, "Camila Torres", 12500, 7, False)
        assert suite_premium.calcular_costo() == 87500
    
    def test_suite_premium_con_jacuzzi(self):
        # Prueba el cálculo de costo para una suite premium con jacuzzi
        suite_premium = SuitePremium(301, "Luis Fernandez", 12000, 2, True)
        assert suite_premium.calcular_costo() == 28800
    
    def test_obtener_suma_reservas(self, hotel):
        # Prueba que la suma de todas las reservas sea la esperada
        suma = hotel.obtener_suma_reservas()
        assert suma == 217700
    
    def test_reserva_mas_cara(self, hotel):
        # Prueba que la reserva más cara sea la correcta
        reserva_cara = hotel.obtener_reserva_mas_cara()
        assert reserva_cara.numero == 302
        assert reserva_cara.huesped == "Camila Torres"
        assert reserva_cara.calcular_costo_total() == 87500
    
    def test_ingreso_total_hotel(self, hotel):
        # Prueba que el ingreso total del hotel sea el esperado
        ingreso_total = hotel.calcular_ingreso_total()
        assert ingreso_total == 217700
    
    def test_contar_suites_vista_mar(self, hotel):
        # Prueba que cuente correctamente las suites con vista al mar
        suites_vista_mar = hotel.contar_suites_vista_mar()
        assert suites_vista_mar == 1
    
    def test_contar_suites_premium_jacuzzi(self, hotel):
        # Prueba que cuente correctamente las suites premium con jacuzzi
        suites_premium_jacuzzi = hotel.contar_suites_premium_jacuzzi()
        assert suites_premium_jacuzzi == 1
    
    def test_herencia_habitaciones(self):
        # Verifica que las clases Estandar, Suite y SuitePremium heredan de Habitacion
        assert issubclass(Estandar, Habitacion)
        assert issubclass(Suite, Habitacion)
        assert issubclass(SuitePremium, Habitacion)
    
    def test_composicion_hotel_habitaciones(self, hotel):
        # Verifica que el hotel tenga el atributo habitaciones y que cada elemento sea una instancia de Habitacion
        assert hasattr(hotel, 'habitaciones')
        for habitacion in hotel.habitaciones:
            assert isinstance(habitacion, Habitacion)
    
    def test_atributos_habitacion_estandar(self):
        # Verifica los atributos de una habitación estándar
        habitacion = Estandar(101, "Juan Perez", 5000, 3, False)
        assert habitacion.tipo == 1
        assert habitacion.numero == 101
        assert habitacion.huesped == "Juan Perez"
        assert habitacion.costo_base == 5000
        assert habitacion.noches == 3
    
    def test_atributos_suite(self):
        # Verifica los atributos de una suite
        suite = Suite(201, "Carlos Gomez", 8000, 5, True)
        assert suite.tipo == 2
        assert suite.vista_mar == True
    
    def test_atributos_suite_premium(self):
        # Verifica los atributos de una suite premium
        suite_premium = SuitePremium(301, "Luis Fernandez", 12000, 2, True)
        assert suite_premium.tipo == 3
        assert suite_premium.jacuzzi == True
