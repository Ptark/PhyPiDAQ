from ..item import SensorItem
from ..config import ConfigModel, EnumOption, NumOption
from phypidaq import ADS1115Config


class ForceSensorItem(SensorItem):
    def __init__(self):
        name: str = "Kraftsensor"
        description: str = "Der Kraftsensor misst die Kraft in Newton"
        config: ConfigModel = ConfigModel.ConfigModel()
        self.__config.add_num_option(NumOption.NumOption("Ausleserate", 100))
        super().__init__(name, description, config, 1, ADS1115Config())

    def get_unit(self) -> str:
        if self._config.enum_options[0] is not None:
            e_opt: EnumOption = self._config.enum_options[0]
            if e_opt.selection == 'Kelvin':
                return "K"
            return "°C"
        return ""
