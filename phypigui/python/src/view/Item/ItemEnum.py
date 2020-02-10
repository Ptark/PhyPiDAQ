from abc import ABC
from enum import Enum, unique
from typing import Type

from PyQt5.QtWidgets import QWidget

from ...SystemInfo import SystemInfo
from ...model.item.AccelerationSensorItem import AccelerationSensorItem
from ...model.item.ConstantItems import ConstantItem, NatureConstantItem
from ...model.item.CurrentSensorItem import CurrentSensorItem
from ...model.item.DiagramItem import DiagramItem, TimeDiagramItem, DualDiagramItem, BarDiagramItem
from ...model.item.DistanceSensorItem import DistanceSensorItem
from ...model.item.ForceSensorItem import ForceSensorItem
from ...model.item.ItemModel import ItemModel
from ...model.item.OperatorItem import AdditionOperatorItem, SubtractionOperatorItem, \
    MultiplicationOperatorItem, DivisionOperatorItem, AbsoluteOperatorItem, OperatorItem, NegativeOperatorItem, \
    PowerOperatorItem, RootOperatorItem, CloneItem
from ...model.item.ProxySensorItem import ProxySensorItem
from ...model.item.RGBSensorItem import RGBSensorItem
from ...model.item.SensorItem import SensorItem
from ...model.item.TemperatureSensorItem import TemperatureSensorItem
from ...model.item.VoltageSensorItem import VoltageSensorItem
from ..DiagramField.DiagramView import DiagramView, TimeDiagram, DualDiagram, BarDiagram
from .DiagramItemView import DiagramItemView
from .OperatorItemView import OperatorItemView
from .SensorItemView import SensorItemView
from .WorkspaceItemView import WorkspaceItemView
from ...model.item.WriteToFileItem import WriteToFileItem


class ItemEnumMeta(type(ABC), type(Enum)):
    pass


@unique
class ItemEnum(ABC, Enum, metaclass=ItemEnumMeta):
    def __init__(self, view: Type[WorkspaceItemView], model: Type[ItemModel], file: str):
        self.__view: Type[WorkspaceItemView] = view
        self.__model: Type[ItemModel] = model
        self.__path: str = SystemInfo.RESOURCES + 'images/items/' + file + '.svg'

    @property
    def model(self) -> Type[ItemModel]:
        return self.__model

    @property
    def path(self) -> str:
        return self.__path

    def create_workspace_item(self, parent: QWidget) -> WorkspaceItemView:
        return self.__view(parent, self)


@unique
class SensorEnum(ItemEnum):
    PROXY_SENSOR = (ProxySensorItem, 'file_read')
    CONSTANT = (ConstantItem, 'constant')
    NATURE_CONSTANT = (NatureConstantItem, 'nature_constant')
    TEMPERATURE_SENSOR = (TemperatureSensorItem, 'temperature')
    FORCE_SENSOR = (ForceSensorItem, 'force')
    DISTANCE_SENSOR = (DistanceSensorItem, 'distance')
    ACCELERATION_SENSOR = (AccelerationSensorItem, 'acceleration')
    CURRENT_SENSOR = (CurrentSensorItem, 'current')
    RGB_SENSOR = (RGBSensorItem, 'rgb')
    VOLTAGE_SENSOR = (VoltageSensorItem, 'voltage')

    def __init__(self, model: Type[SensorItem], file: str):
        super().__init__(SensorItemView, model, 'sensor/' + file)


@unique
class OperatorEnum(ItemEnum):
    ADDITION_OPERATOR = (AdditionOperatorItem, 'addition')
    SUBTRACTION_OPERATOR = (SubtractionOperatorItem, 'subtraction')
    MULTIPLICATION_OPERATOR = (MultiplicationOperatorItem, 'multiplication')
    DIVISION_OPERATOR = (DivisionOperatorItem, 'division')
    ABSOLUTE_OPERATOR = (AbsoluteOperatorItem, 'absolute')
    NEGATIVE_OPERATOR = (NegativeOperatorItem, 'negative')
    POWER_OPERATOR = (PowerOperatorItem, 'power')
    ROOT_OPERATOR = (RootOperatorItem, 'root')
    CLONE_OPERATOR = (CloneItem, 'clone')

    def __init__(self, model: Type[OperatorItem], file: str):
        super().__init__(OperatorItemView, model, 'operator/' + file)


@unique
class DiagramEnum(ItemEnum):
    WRITE_TO_FILE = (WriteToFileItem, 'file_write', None)
    TIME_DIAGRAM = (TimeDiagramItem, 'time', TimeDiagram)
    DUAL_DIAGRAM = (DualDiagramItem, 'dual', DualDiagram)
    BAR_DIAGRAM = (BarDiagramItem, 'bar', BarDiagram)

    def __init__(self, model: Type[DiagramItem], file: str, diagram: Type[DiagramView]):
        self.__diagram: Type[DiagramView] = diagram
        super().__init__(DiagramItemView, model, 'diagram/' + file)

    @property
    def diagram(self) -> Type[DiagramView]:
        return self.__diagram