from abc import ABC
from enum import Enum, unique
from typing import Type

from PyQt5.QtWidgets import QWidget

from ...SystemInfo import SystemInfo
from phypigui.python.src.model.item.SensorItems.AccelerationSensorItem import AccelerationSensorItem
from phypigui.python.src.model.item.SensorItems.ConstantItems import ConstantItem, NatureConstantItem
from phypigui.python.src.model.item.SensorItems.CurrentSensorItem import CurrentSensorItem
from phypigui.python.src.model.item.DiagramItems.DiagramItem import DiagramItem
from phypigui.python.src.model.item.DiagramItems.TimeDiagramItem import TimeDiagramItem
from phypigui.python.src.model.item.DiagramItems.DualDiagramItem import DualDiagramItem
from phypigui.python.src.model.item.DiagramItems.BarDiagramItem import BarDiagramItem
from phypigui.python.src.model.item.SensorItems.DistanceSensorItem import DistanceSensorItem
from phypigui.python.src.model.item.SensorItems.ForceSensorItem import ForceSensorItem
from ...model.item.ItemModel import ItemModel
from phypigui.python.src.model.item.OperatorItems.OperatorItem import OperatorItem
from phypigui.python.src.model.item.OperatorItems.AdditionOperatorItem import AdditionOperatorItem
from phypigui.python.src.model.item.OperatorItems.SubtractionOperatorItem import SubtractionOperatorItem
from phypigui.python.src.model.item.OperatorItems.MultiplicationOperatorItem import MultiplicationOperatorItem
from phypigui.python.src.model.item.OperatorItems.DivisionOperatorItem import DivisionOperatorItem
from phypigui.python.src.model.item.OperatorItems.AbsoluteOperatorItem import AbsoluteOperatorItem
from phypigui.python.src.model.item.OperatorItems.NegativeOperatorItem import NegativeOperatorItem
from phypigui.python.src.model.item.OperatorItems.PowerOperatorItem import PowerOperatorItem
from phypigui.python.src.model.item.OperatorItems.RootOperatorItem import RootOperatorItem
from phypigui.python.src.model.item.OperatorItems.CloneItem import CloneItem
from phypigui.python.src.model.item.SensorItems.ProxySensorItem import ProxySensorItem
from phypigui.python.src.model.item.SensorItems.RGBSensorItem import RGBSensorItem
from phypigui.python.src.model.item.SensorItems.SensorItem import SensorItem
from phypigui.python.src.model.item.SensorItems.TemperatureSensorItem import TemperatureSensorItem
from phypigui.python.src.model.item.SensorItems.VoltageSensorItem import VoltageSensorItem
from ..DiagramField.DiagramView import DiagramView, TimeDiagram, DualDiagram, BarDiagram
from .DiagramItemView import DiagramItemView
from .OperatorItemView import OperatorItemView
from .SensorItemView import SensorItemView
from .WorkspaceItemView import WorkspaceItemView
from phypigui.python.src.model.item.DiagramItems.WriteToFileItem import WriteToFileItem


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
