"""Platform for SolarMAN logger sensor integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.util.dt import utc_from_timestamp
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass,
    SensorDeviceClass,
)
from homeassistant.const import (
    # DEVICE_CLASS_FREQUENCY,
    # DEVICE_CLASS_TIME,
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfFrequency,
    UnitOfEnergy,
    UnitOfTime,
)

from .const import (
    DOMAIN,
    SENSOR_VDC1,
    SENSOR_IDC1,
    SENSOR_VDC2,
    SENSOR_IDC2,
    SENSOR_VAC,
    SENSOR_IAC,
    SENSOR_FREQ,
    SENSOR_TEMP,
    SENSOR_PWR,
    SENSOR_ENERGY_DAY,
    SENSOR_ENERGY_TOT,
    SENSOR_HRS,
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the SolarMAN logger sensor platform."""
    sensors = []
    sensors.append(
        SolarMANSensor(
            SENSOR_VDC1,
            SensorDeviceClass.VOLTAGE,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_IDC1,
            SensorDeviceClass.CURRENT,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_VDC2,
            SensorDeviceClass.VOLTAGE,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_IDC2,
            SensorDeviceClass.CURRENT,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_VAC,
            SensorDeviceClass.VOLTAGE,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricPotential.VOLT,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_IAC,
            SensorDeviceClass.CURRENT,
            SensorStateClass.MEASUREMENT,
            UnitOfElectricCurrent.AMPERE,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_FREQ,
            None,
            SensorStateClass.MEASUREMENT,
            UnitOfFrequency.HERTZ,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_TEMP,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfTemperature.CELSIUS,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_PWR,
            SensorDeviceClass.POWER,
            SensorStateClass.MEASUREMENT,
            UnitOfPower.WATT,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_ENERGY_DAY,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfEnergy.WATT_HOUR,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_ENERGY_TOT,
            SensorDeviceClass.ENERGY,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfEnergy.KILO_WATT_HOUR,
            entry.unique_id,
        )
    )
    sensors.append(
        SolarMANSensor(
            SENSOR_HRS,
            None,
            SensorStateClass.TOTAL_INCREASING,
            UnitOfTime.HOURS,
            entry.unique_id,
        )
    )
    hass.data[DOMAIN][entry.entry_id].sensors = sensors
    async_add_entities(sensors)


class SolarMANSensor(SensorEntity):
    """Representation of a SolarMAN logger device."""

    def __init__(self, name, device_class, state_class, unit, uid):
        """Initialize the sensor."""
        self._name = name
        self._device_class = device_class
        self._state_class = state_class
        self._unit = unit
        self._uid = uid
        self.online = False
        self.value = 0

    @property
    def unique_id(self):
        """Return unique id."""
        return f"{DOMAIN}_{self._name}"

    @property
    def name(self):
        """Name of this inverter attribute."""
        return self._name

    @property
    def device_info(self) -> DeviceInfo:
        """Information about this device."""
        return {
            "identifiers": {(DOMAIN, self._uid)},
            "name": "SolarMAN",
            "model": "Logger",
            "manufacturer": "IGEN Tech",
        }

    @property
    def device_class(self):
        """State of this inverter attribute."""
        return self._device_class

    @property
    def state_class(self):
        """State of this inverter attribute."""
        return self._state_class

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def native_value(self):
        """State of this inverter attribute."""
        return self.value

    @property
    def should_poll(self) -> bool:
        """No polling needed."""
        return False

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.online
