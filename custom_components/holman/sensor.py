"""Platform for light integration."""
import logging

import holman

from homeassistant.helpers.entity import Entity

#import homeassistant.helpers.config_validation as cv
# Import the device class from the component that you want to support
#3from homeassistant.components.switch import (
#3    ATTR_BRIGHTNESS, PLATFORM_SCHEMA, Light)
#from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
#PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
#    vol.Required(CONF_HOST): cv.string,
#    vol.Optional(CONF_USERNAME, default='admin'): cv.string,
 #   vol.Optional(CONF_PASSWORD): cv.string,
#})

class TapTimerManagerPrintListener(holman.TapTimerManagerListener):
    def tap_timer_discovered(self, tap_timer):
        print("Discovered Holman tap_timer", tap_timer.mac_address)

def setup_platform(hass, config, add_entities, discovery_info=None):
	

	manager = holman.TapTimerManager()
	manager.listener = TapTimerManagerPrintListener()
	manager.start_discovery()
	manager.run()
    # Assign configuration variables.
    # The configuration check takes care they are present.
    mac_addr = '00:00:00:00:00:00'
	#host = config[CONF_HOST]
    #username = config[CONF_USERNAME]
    #password = config.get(CONF_PASSWORD)

    # Setup connection with devices/cloud
    #hub = awesomelights.Hub(host, username, password)

    # Verify that passed in configuration works
    #if not hub.is_valid_login():
    #    _LOGGER.error("Could not connect to AwesomeLight hub")
    #    return

    # Add devices
    #add_entities(AwesomeLight(light) for light in hub.lights())
	add_entities([Holman()])


class Holman(Entity):
    """Representation of an Awesome Light."""

    def __init__(self):
        """Initialize an AwesomeLight."""
		self._mac = '00:00:00:00:00:00'
        #self._light = light
        #self._name = light.name
        #self._state = None
        #self._brightness = None

    @property
    def name(self):
        """Return the display name of this light."""
        return 'Holman'+self._mac

    @property
    def state(self):
        """Return the state of the sensor."""
        return False
		
	@property
    def is_on(self):
        """Return true if light is on."""
        return False

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return None

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
		"""
		manager = holman.TapTimerManager(adapter_name='hci0')

		tap_timer = holman.TapTimer(mac_address='AA:BB:CC:DD:EE:FF', manager=manager)
		tap_timer.listener = holman.TapTimerListener() # Use an instance of your own holman.TapTimerListener subclass
		tap_timer.connect()

		manager.run()

		TapTimer.start(runtime=1)
		"""
        self._state = 23
