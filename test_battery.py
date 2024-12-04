import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def describe_Battery():

    def describe_Battery_with_monitor():

        def test_recharge_calls_notify_recharge_correctly():
            external_monitor_mock = Mock()

            battery = Battery(100, external_monitor=external_monitor_mock)

            battery.drain(50)
            battery.recharge(30)

            external_monitor_mock.notify_recharge.assert_called_once_with(80)

        def test_drain_calls_notify_drain_correctly():
            external_monitor_mock = Mock()

            battery = Battery(100, external_monitor=external_monitor_mock)

            battery.drain(70)

            external_monitor_mock.notify_drain.assert_called_once_with(30)

    

    def describe_test_constructor():

        def describe_recharge():
            def normal_battery_activity():
                bat = Battery(100)
                bat.drain(50)
                assert bat.getCharge() == 50
                bat.recharge(50)
                assert bat.getCharge() == 100

            def big_init_number():
                bat = Battery(1000000000)
                bat.drain(50)
                assert bat.getCharge() == 999999950
                bat.recharge(50)
                assert bat.getCharge() == 1000000000

            def small_init_number():
                bat = Battery(2)
                bat.drain(1)
                assert bat.getCharge() == 1
                bat.recharge(2)
                assert bat.getCharge() == 2
            
            def neg_number():
                bat = Battery(100)
                bat.drain(50)
                assert bat.getCharge() == 50
                bat.recharge(-50)
                assert bat.getCharge() == 50

            def charge_too_high():
                #would be TOO charged (ie would go over the capacity)
                bat = Battery(100)
                bat.drain(50)
                assert bat.getCharge() == 50
                bat.recharge(500)
                assert bat.getCharge() == 100



        def describe_drain():
            def normal_drain_activity():
                b = Battery(100)
                b.drain(50)
                assert b.getCharge() == 50

            def big_init_number():
                b = Battery(10000000)
                b.drain(50)
                assert b.getCharge() == 10000000 - 50

            def small_init_number():
                b = Battery(2)
                b.drain(1)
                assert b.getCharge() == 1
            
            def neg_number():
                b = Battery(100)
                b.drain(-50)
                assert b.getCharge() == 100

            def charge_too_low():
                # not enough battery to drain the amount
                b = Battery(49)
                b.drain(50)
                assert b.getCharge() == 0
        
        def describe_get_charge():
            def get_charge_is_working_as_intended():
                b = Battery(10)
                assert b.getCharge() == 10

        def describe_get_capacity():
            def get_capacity_is_working_as_intended():
                b = Battery(10)
                assert b.getCapacity() == 10

        def describe_init():
            def init_as_a_postitive():
                b = Battery(10)
                assert b.getCapacity() == 10 and b.getCharge() == 10

            def init_wont_take_neg():
                b = Battery(-19)
                

                def test_square_root_value_error(): 
                    with pytest.raises(ValueError) as excinfo:  
                        b = Battery(-1)  
                    assert str(excinfo.value) == "Neg not allowed"  


